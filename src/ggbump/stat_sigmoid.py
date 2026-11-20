from __future__ import annotations

from typing import TYPE_CHECKING, Any

import pandas as pd
from plotnine.stats.stat import stat
from typing_extensions import override

from ._sigmoid import check_direction, sigmoid

if TYPE_CHECKING:
    from plotnine.iapi import pos_scales

__all__ = ["stat_sigmoid"]


# plotnine declares REQUIRED_AES, DEFAULT_PARAMS and CREATES as plain class attributes (RUF012).
class stat_sigmoid(stat):
    """
    A sigmoid curve from (x, y) to (xend, yend) for every row

    Parameters
    ----------
    mapping :
        Aesthetic mappings: ``x``, ``y``, ``xend`` and ``yend`` are required.
    data :
        The data for this layer.
    geom :
        The geom that draws the curves (default ``"line"``).
    smooth :
        How steep the curve is: higher means a sharper step in the middle.
    direction :
        ``"x"`` (default) smooths along x, ``"y"`` along y.
    **kwargs :
        Passed to the geom.
    """

    REQUIRED_AES: set[str] = {"x", "y", "xend", "yend"}  # noqa: RUF012
    DEFAULT_PARAMS: dict[str, Any] = {  # noqa: RUF012
        "geom": "line",
        "position": "identity",
        "na_rm": False,
        "smooth": 8,
        "direction": "x",
    }

    @override
    def setup_params(self, data: pd.DataFrame) -> None:
        check_direction(self.params["direction"])

    @override
    def setup_data(self, data: pd.DataFrame) -> pd.DataFrame:
        # every row is its own curve, numbered within its panel
        data = data.copy()
        data["group"] = data.groupby("PANEL", observed=True).cumcount() + 1
        return data

    @override
    def compute_group(self, data: pd.DataFrame, scales: pos_scales) -> pd.DataFrame:
        smooth: Any = self.params["smooth"]
        direction: Any = self.params["direction"]
        row = data.iloc[0]
        return sigmoid(
            row["x"],
            row["xend"],
            row["y"],
            row["yend"],
            smooth=smooth,
            direction=direction,
        )
