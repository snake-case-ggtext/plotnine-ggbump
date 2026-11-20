"""
ggbump: a Python (plotnine) port of the R package ggbump.

Bump charts and sigmoid curves as plotnine geoms and stats.
"""

from __future__ import annotations

from ._sigmoid import rank_sigmoid, sigmoid
from .geoms import geom_bump, geom_sigmoid
from .stat_bump import stat_bump
from .stat_sigmoid import stat_sigmoid

__version__ = "0.1.0"

__all__ = [
    "geom_bump",
    "geom_sigmoid",
    "rank_sigmoid",
    "sigmoid",
    "stat_bump",
    "stat_sigmoid",
]
