"""sigmoid() and rank_sigmoid(); expected values computed with R ggbump 0.1.99999."""

from __future__ import annotations

from collections.abc import Callable

import numpy as np
import pytest

from ggbump import rank_sigmoid, sigmoid


def test_sigmoid_x():
    # R: sigmoid(0, 3, 1, 5, smooth = 5, n = 5)
    out = sigmoid(0, 3, 1, 5, smooth=5, n=5)
    assert list(out.columns) == ["x", "y"]
    np.testing.assert_allclose(out["x"], [0, 0.75, 1.5, 2.25, 3])
    np.testing.assert_allclose(
        out["y"],
        [1.02677140369714, 1.30343272008497, 3, 4.69656727991503, 4.97322859630286],
    )


def test_sigmoid_y():
    # R: sigmoid(0, 3, 1, 5, smooth = 4, n = 4, direction = "y")
    out = sigmoid(0, 3, 1, 5, smooth=4, n=4, direction="y")
    assert list(out.columns) == ["y", "x"]
    np.testing.assert_allclose(out["y"], [1, 2.33333333333333, 3.66666666666667, 5])
    np.testing.assert_allclose(
        out["x"],
        [
            0.0539586298862747,
            0.6258255819781346,
            2.3741744180218651,
            2.9460413701137256,
        ],
    )


def test_sigmoid_defaults():
    out = sigmoid(0, 1, 0, 1)
    assert len(out) == 100
    # smooth = 5 by default: the curve stops 1 / (1 + e^5) short of each end
    np.testing.assert_allclose(out["y"].iloc[0], 1 / (1 + np.exp(5)))


def test_rank_sigmoid():
    # R: rank_sigmoid(c(1, 2, 3), c(3, 1, 2), smooth = 2)[c(1, 50, 100, 101, 200), ]
    out = rank_sigmoid([1, 2, 3], [3, 1, 2], smooth=2)
    assert len(out) == 200
    rows = out.iloc[[0, 49, 99, 100, 199]]
    np.testing.assert_allclose(rows["x"], [1, 1.4949494949495, 2, 2, 3])
    np.testing.assert_allclose(
        rows["y"],
        [
            2.76159415595576,
            2.01010066657831,
            1.23840584404424,
            1.11920292202212,
            1.88079707797788,
        ],
    )


def test_rank_sigmoid_one_point():
    assert len(rank_sigmoid([1], [1])) == 0


@pytest.mark.parametrize(
    "fn",
    [
        lambda: sigmoid(0, 1, 0, 1, direction="z"),  # pyrefly: ignore[bad-argument-type]
        lambda: rank_sigmoid([1, 2], [1, 2], direction="z"),  # pyrefly: ignore[bad-argument-type]
    ],
)
def test_invalid_direction(fn: Callable[[], object]):
    # R: sigmoid(0, 1, 0, 1, direction = "z") errors with this message
    with pytest.raises(ValueError, match="Only the directions x or y is allowed."):
        fn()
