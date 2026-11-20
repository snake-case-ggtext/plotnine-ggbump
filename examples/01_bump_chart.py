"""
Bump chart

Rank over time: one smooth line per country, points at each observation and
labels at both ends. Rank 1 is at the top.
"""

import os
from pathlib import Path

import pandas as pd
from plotnine import (
    aes,
    geom_point,
    geom_text,
    ggplot,
    labs,
    scale_color_manual,
    scale_x_continuous,
    scale_y_reverse,
    theme,
    theme_minimal,
)

from ggbump import geom_bump

OUT = Path(
    os.environ.get(
        "GGBUMP_EXAMPLES_OUT", Path(__file__).parent.parent / "docs" / "images"
    )
)
OUT.mkdir(parents=True, exist_ok=True)

df = pd.DataFrame(
    {
        "country": ["India"] * 3 + ["Sweden"] * 3 + ["Germany"] * 3 + ["Finland"] * 3,
        "year": [2011, 2012, 2013] * 4,
        "rank": [4, 2, 2, 3, 1, 4, 2, 3, 1, 1, 4, 3],
    }
)
first, last = df[df["year"] == 2011], df[df["year"] == 2013]

p = (
    ggplot(df, aes("year", "rank", color="country"))
    + geom_bump(size=2, smooth=8)
    + geom_point(size=6)
    + geom_text(aes(x="year - .12", label="country"), data=first, ha="right", size=11)
    + geom_text(aes(x="year + .12", label="country"), data=last, ha="left", size=11)
    + scale_x_continuous(limits=(2010.5, 2013.5), breaks=[2011, 2012, 2013])
    + scale_y_reverse()
    + scale_color_manual(values=["#F1BB7B", "#FD6467", "#5B1A18", "#D67236"])
    + labs(x="", y="RANK")
    + theme_minimal()
    + theme(legend_position="none", figure_size=(8, 3.5))
)
p.save(OUT / "bump_chart.png", dpi=100, verbose=False)
