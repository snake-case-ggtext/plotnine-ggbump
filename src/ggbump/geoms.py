from __future__ import annotations

from typing import TYPE_CHECKING, Any
from warnings import warn

from plotnine.exceptions import PlotnineWarning
from plotnine.geoms.geom_line import geom_line
from typing_extensions import override

if TYPE_CHECKING:
    import pandas as pd
    from plotnine.mapping.aes import aes
    from plotnine.typing import DataLike

__all__ = ["geom_bump", "geom_sigmoid"]

# R argument spellings accepted as aliases for plotnine's
R_ALIASES = {"linewidth": "size"}


def _translate(kwargs: dict[str, Any]) -> dict[str, Any]:
    for r_name, name in R_ALIASES.items():
        if r_name in kwargs:
            kwargs.setdefault(name, kwargs.pop(r_name))
    return kwargs


class _sigmoid_line(geom_line):
    def __init__(
        self, mapping: aes | None = None, data: DataLike | None = None, **kwargs: Any
    ):
        super().__init__(mapping, data, **_translate(kwargs))
        # smooth and direction are parameters; mapped, they would be silently ignored (R warns too)
        if self.mapping is not None:
            ignored = sorted({"smooth", "direction"} & set(self.mapping))
            if ignored:
                warn(
                    f"Ignoring unknown aesthetics: {', '.join(ignored)}",
                    PlotnineWarning,
                    stacklevel=2,
                )

    @override
    def setup_data(self, data: pd.DataFrame) -> pd.DataFrame:
        # R's order() is stable; a stable sort keeps vertical runs (ties in x) in drawing order
        return data.sort_values(["PANEL", "group", "x"], kind="mergesort")


class geom_bump(_sigmoid_line):
    """
    Bump chart: lines that step smoothly from point to point

    Use it to show rank over time: map ``x`` to time, ``y`` to rank and ``color``
    to the thing being ranked.

    Parameters
    ----------
    mapping :
        Aesthetic mappings: ``x`` and ``y`` are required.
    data :
        The data for this layer.
    smooth :
        How steep each step is: higher means a sharper step in the middle
        (default 8).
    direction :
        ``"x"`` (default) smooths along x; ``"y"`` along y.
    **kwargs :
        Other parameters and aesthetics, as for `geom_line`. ``linewidth`` is
        accepted as an alias for ``size``.
    """

    DEFAULT_PARAMS = geom_line.DEFAULT_PARAMS | {"stat": "bump"}


class geom_sigmoid(_sigmoid_line):
    """
    A sigmoid curve from (x, y) to (xend, yend) for every row

    Parameters
    ----------
    mapping :
        Aesthetic mappings: ``x``, ``y``, ``xend`` and ``yend`` are required.
    data :
        The data for this layer.
    smooth :
        How steep the curve is: higher means a sharper step in the middle
        (default 8).
    direction :
        ``"x"`` (default) smooths along x; ``"y"`` along y.
    **kwargs :
        Other parameters and aesthetics, as for `geom_line`. ``linewidth`` is
        accepted as an alias for ``size``.
    """

    DEFAULT_PARAMS = geom_line.DEFAULT_PARAMS | {"stat": "sigmoid"}
