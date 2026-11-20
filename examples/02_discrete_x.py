"""
Ordered categories on the x axis

geom_bump works with a categorical x too. Each step is drawn between a
player's consecutive seasons, in the order of the categories. `smooth`
sets how sharp each step is.
"""

import os
from pathlib import Path

import pandas as pd
from plotnine import (
    aes,
    geom_point,
    ggplot,
    labs,
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

seasons = ["Spring", "Pre-season", "Summer", "Season finale", "Autumn", "Winter"]
df = pd.DataFrame(
    {
        "season": pd.Categorical(seasons * 4, categories=seasons),
        "rank": [
            1,
            3,
            4,
            2,
            1,
            4,
            2,
            4,
            1,
            3,
            2,
            3,
            4,
            1,
            2,
            4,
            4,
            1,
            3,
            2,
            3,
            1,
            3,
            2,
        ],
        "player": [p for p in ("David", "Anna", "Franz", "Ika") for _ in seasons],
    }
)

p = (
    ggplot(df, aes("season", "rank", color="player"))
    + geom_bump(size=2, smooth=20, show_legend=False)
    + geom_point(aes(shape="player"), size=5)
    + scale_y_reverse()
    + labs(x="", y="Rank", color="Player", shape="Player")
    + theme_minimal()
    + theme(figure_size=(8, 3))
)
p.save(OUT / "discrete_x.png", dpi=100, verbose=False)
