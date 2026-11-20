"""
Sigmoid curves

geom_sigmoid draws one curve per row, from (x, y) to (xend, yend).
`direction="y"` smooths along y instead of x.
"""

import os
from pathlib import Path

import pandas as pd
from plotnine import aes, ggplot, labs, theme, theme_minimal

from ggbump import geom_sigmoid

OUT = Path(
    os.environ.get(
        "GGBUMP_EXAMPLES_OUT", Path(__file__).parent.parent / "docs" / "images"
    )
)
OUT.mkdir(parents=True, exist_ok=True)

df = pd.DataFrame(
    {"x": range(1, 7), "y": range(5, 11), "xend": 7, "yend": range(-3, 3)}
)


def sigmoids(direction: str) -> ggplot:
    return (
        ggplot(df, aes(x="x", xend="xend", y="y", yend="yend", color="factor(x)"))
        + geom_sigmoid(size=1.5, direction=direction)
        + labs(color="x", title=f'direction = "{direction}"')
        + theme_minimal()
        + theme(figure_size=(5, 3.5))
    )


sigmoids("x").save(OUT / "sigmoid_x.png", dpi=100, verbose=False)
sigmoids("y").save(OUT / "sigmoid_y.png", dpi=100, verbose=False)
