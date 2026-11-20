"""Sigmoid curves between points: the maths behind geom_bump and geom_sigmoid.

Translated from R ggbump's ``sigmoid()`` and ``rank_sigmoid()`` (MIT, David Sjöberg).
"""

from __future__ import annotations

from typing import Literal

import numpy as np
import pandas as pd

Direction = Literal["x", "y"]

__all__ = ["rank_sigmoid", "sigmoid"]


def check_direction(direction: str) -> None:
    if direction not in ("x", "y"):
        msg = "Only the directions x or y is allowed."
        raise ValueError(msg)


def sigmoid(
    x_from: float,
    x_to: float,
    y_from: float,
    y_to: float,
    smooth: float = 5,
    n: int = 100,
    direction: Direction = "x",
) -> pd.DataFrame:
    """
    Points on a smooth sigmoid curve from ``(x_from, y_from)`` to ``(x_to, y_to)``.

    The curve is the logistic function sampled at ``n`` points over
    ``[-smooth, smooth]``, rescaled to the two points.

    Parameters
    ----------
    x_from, x_to, y_from, y_to :
        Start and end of the curve.
    smooth :
        How steep the curve is: higher means a sharper step in the middle.
    n :
        Number of points.
    direction :
        ``"x"`` smooths along x (the curve leaves and arrives horizontally);
        ``"y"`` smooths along y.

    Returns
    -------
    :
        Columns ``x`` and ``y`` (``y`` first for ``direction="y"``, as in R).
    """
    check_direction(direction)
    t = np.linspace(-smooth, smooth, n)
    s = np.exp(t) / (np.exp(t) + 1)
    along = (t + smooth) / (smooth * 2)
    if direction == "x":
        return pd.DataFrame(
            {"x": along * (x_to - x_from) + x_from, "y": s * (y_to - y_from) + y_from}
        )
    return pd.DataFrame(
        {"y": along * (y_to - y_from) + y_from, "x": s * (x_to - x_from) + x_from}
    )


def rank_sigmoid(
    x: pd.Series | np.ndarray | list[float],
    y: pd.Series | np.ndarray | list[float],
    smooth: float = 8,
    direction: Direction = "x",
) -> pd.DataFrame:
    """
    A sigmoid curve joining each point to the next, in the order given.

    Parameters
    ----------
    x, y :
        The points.
    smooth :
        How steep each step is: higher means a sharper step in the middle.
    direction :
        ``"x"`` or ``"y"``; see [](`~ggbump.sigmoid`).

    Returns
    -------
    :
        Columns ``x`` and ``y``, 100 rows per step.
    """
    check_direction(direction)
    xs = np.asarray(x, dtype=float)
    ys = np.asarray(y, dtype=float)
    steps = [
        sigmoid(xs[i - 1], xs[i], ys[i - 1], ys[i], smooth=smooth, direction=direction)
        for i in range(1, len(xs))
        if not np.isnan(xs[i - 1])
    ]
    if not steps:
        return pd.DataFrame({"x": [], "y": []})
    return pd.concat(steps, ignore_index=True)
