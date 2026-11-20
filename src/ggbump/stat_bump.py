from __future__ import annotations

from typing import TYPE_CHECKING, Any

import numpy as np
import pandas as pd
from plotnine.stats.stat import stat
from typing_extensions import override

from ._sigmoid import check_direction, rank_sigmoid, sigmoid

if TYPE_CHECKING:
    from plotnine.iapi import pos_scales

__all__ = ["stat_bump"]


# plotnine declares REQUIRED_AES, DEFAULT_PARAMS and CREATES as plain class attributes (RUF012).
class stat_bump(stat):
    """
    Smooth sigmoid steps between consecutive points of each line

    Parameters
    ----------
    mapping :
        Aesthetic mappings: ``x`` and ``y`` are required.
    data :
        The data for this layer.
    geom :
        The geom that draws the curves (default ``"line"``).
    smooth :
        How steep each step is: higher means a sharper step in the middle.
    direction :
        ``"x"`` (default) smooths along x, ``"y"`` along y.
    **kwargs :
        Passed to the geom.

    Notes
    -----
    A line is the set of rows sharing every aesthetic other than position.
    With a discrete x each (x, line) pair is its own group, so each group draws
    the step from the line's previous x to its own.
    """

    REQUIRED_AES: set[str] = {"x", "y"}  # noqa: RUF012
    DEFAULT_PARAMS: dict[str, Any] = {  # noqa: RUF012
        "geom": "line",
        "position": "identity",
        "na_rm": False,
        "smooth": 8,
        "direction": "x",
    }
    CREATES: set[str] = {"x_lag", "y_lag"}  # noqa: RUF012

    @override
    def setup_params(self, data: pd.DataFrame) -> None:
        check_direction(self.params["direction"])

    @override
    def setup_data(self, data: pd.DataFrame) -> pd.DataFrame:
        # Lag x and y within each line, in x order. A line is every row sharing the
        # non-position columns, so this works across groups (needed for discrete x).
        data = data.reset_index(drop=True)
        keys = [c for c in data.columns if c not in {"PANEL", "group", "x", "y"}]
        ordered = data.sort_values("x", kind="mergesort")
        if keys:
            lagged = ordered.groupby(keys, sort=False, dropna=False)[["x", "y"]].shift()
        else:
            lagged = ordered[["x", "y"]].shift()
        data["x_lag"] = lagged["x"]
        data["y_lag"] = lagged["y"]
        return data

    @override
    def compute_group(self, data: pd.DataFrame, scales: pos_scales) -> pd.DataFrame:
        smooth: Any = self.params["smooth"]
        direction: Any = self.params["direction"]
        data = data.sort_values("x", kind="mergesort")
        if len(data) == 1:
            row = data.iloc[0]
            if np.isnan(row["x_lag"]) or np.isnan(row["y_lag"]):
                return pd.DataFrame({"x": [], "y": []})
            return sigmoid(
                row["x_lag"],
                row["x"],
                row["y_lag"],
                row["y"],
                smooth=smooth,
                direction=direction,
            )
        return rank_sigmoid(data["x"], data["y"], smooth=smooth, direction=direction)
