"""Port of R ggbump's tests/testthat/test-numeric_inputs.R, plus built-data checks against R.

Adapted: R checks class(p) == c("gg", "ggplot"); here each plot is built and drawn.
Adapted: R's built data repeats each continuous-x curve once per input row (600 rows per country);
the port draws each curve once (200 rows). See docs/differences.md.
"""

from __future__ import annotations

import warnings
from copy import deepcopy

import numpy as np
import pandas as pd
import pytest
from plotnine import aes, facet_wrap, geom_point, ggplot
from plotnine.exceptions import PlotnineWarning

from ggbump import geom_bump, geom_sigmoid, stat_bump

DF = pd.DataFrame(
    {
        "country": ["India"] * 3 + ["Sweden"] * 3 + ["Germany"] * 3 + ["Finland"] * 3,
        "year": [2011, 2012, 2013] * 4,
        "month": ["January", "July", "November"] * 4,
        "rank": [4, 2, 2, 3, 1, 4, 2, 3, 1, 1, 4, 3],
    }
)
DF_SIG = pd.DataFrame({"xend": range(1, 11), "y": 1, "x": 1, "yend": range(10, 0, -1)})


def built(p: ggplot, i: int = 0) -> pd.DataFrame:
    q = deepcopy(p)
    q._setup()
    q._build()
    return q.layers[i].data


def draws(p: ggplot) -> None:
    with warnings.catch_warnings():
        warnings.simplefilter("error")
        p.draw()


def test_basic_usage():
    # Port of test-numeric_inputs.R::"Basic usage"
    draws(
        ggplot(DF, aes("year", "rank", color="country"))
        + geom_point(size=10)
        + geom_bump(size=2)
    )
    sweden = DF[DF["country"] == "Sweden"]
    draws(ggplot(sweden, aes("year", "rank")) + geom_point(size=10) + geom_bump(size=2))
    draws(
        ggplot(sweden, aes("year", "rank"))
        + geom_point(size=10)
        + geom_bump(size=2, smooth=10)
    )


def test_mapped_smooth_warns():
    # Port of test-numeric_inputs.R::"Basic usage" expect_warning(geom_bump(aes(smooth = 10)))
    with pytest.warns(PlotnineWarning, match="Ignoring unknown aesthetics: smooth"):
        geom_bump(aes(smooth=10), size=2)


def test_discrete_x_axis():
    # Port of test-numeric_inputs.R::"Discrete x axis"
    draws(
        ggplot(DF, aes("month", "rank", color="country"))
        + geom_point(size=10)
        + geom_bump(size=2)
    )


def test_geom_sigmoid():
    # Port of test-numeric_inputs.R::"geom_sigmoid"
    draws(
        ggplot(
            DF_SIG, aes(x="x", xend="xend", y="y", yend="yend", color="factor(yend)")
        )
        + geom_sigmoid(size=2)
    )


def test_discrete_x_one_curve_per_step():
    # R: layer_data(ggplot(df, aes(month, rank, color = country)) + geom_bump()) has 800 rows,
    # groups 5..12 (the four January groups draw nothing), 100 rows each, one colour per group
    d = built(ggplot(DF, aes("month", "rank", color="country")) + geom_bump())
    assert len(d) == 800
    assert d.groupby("group").size().tolist() == [100] * 8
    assert (d.groupby("group")["color"].nunique() == 1).all()
    # each step joins a country's consecutive months (January=1, July=2, November=3)
    steps = {
        (g["x"].iloc[0], round(g["y"].iloc[0]), g["x"].iloc[-1], round(g["y"].iloc[-1]))
        for _, g in d.groupby("group")
    }
    expected = set()
    for _, c in DF.groupby("country"):
        r = c["rank"].tolist()
        expected |= {(1.0, r[0], 2.0, r[1]), (2.0, r[1], 3.0, r[2])}
    assert steps == expected


def test_continuous_x_values():
    # Sweden's curve: two sigmoids, 2011 -> 2012 (3 -> 1) and 2012 -> 2013 (1 -> 4)
    d = built(ggplot(DF[DF["country"] == "Sweden"], aes("year", "rank")) + geom_bump())
    assert len(d) == 200
    np.testing.assert_allclose(d["x"].to_numpy()[[0, -1]], [2011, 2013])
    s8 = 1 / (1 + np.exp(8))
    np.testing.assert_allclose(d["y"].iloc[0], 3 - 2 * s8)
    np.testing.assert_allclose(d["y"].iloc[-1], 1 + 3 * (1 - s8))


def test_sigmoid_one_curve_per_row():
    d = built(
        ggplot(DF_SIG, aes(x="x", xend="xend", y="y", yend="yend")) + geom_sigmoid()
    )
    assert d.groupby("group").size().tolist() == [100] * 10


def test_sigmoid_groups_per_panel():
    df = pd.concat([DF_SIG.assign(f="a"), DF_SIG.assign(f="b")])
    d = built(
        ggplot(df, aes(x="x", xend="xend", y="y", yend="yend"))
        + geom_sigmoid()
        + facet_wrap("f")
    )
    assert d.groupby(["PANEL", "group"], observed=True).size().tolist() == [100] * 20


def test_linewidth_alias():
    assert geom_bump(linewidth=3).aes_params["size"] == 3


def test_stat_bump_with_points():
    d = built(
        ggplot(DF, aes("year", "rank", color="country")) + stat_bump(geom="point")
    )
    assert len(d) == 800


@pytest.mark.parametrize("geom", [geom_bump, geom_sigmoid])
def test_invalid_direction(geom: type[geom_bump | geom_sigmoid]):
    p = ggplot(DF_SIG, aes(x="x", xend="xend", y="y", yend="yend")) + geom(
        direction="z"
    )
    with pytest.raises(ValueError, match="Only the directions x or y is allowed."):
        built(p)
