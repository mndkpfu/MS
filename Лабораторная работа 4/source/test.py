import pytest

import statistics

from scipy import stats

import tools
import statools


@pytest.fixture
def samples():
    return tools.read("r4z2.csv", ["X", "Y"])


def test_mean():
    a = [3, 5, 1, -3]
    b = [-4, 2, 7, 0]
    c = [3, -7, -2, 4]

    assert statools.mean(a) == 1.5   # (3+5+1-3)/4 = 1.5
    assert statools.mean(b) == 1.25  # (-4+2+7+0)/4 = 1.25
    assert statools.mean(c) == -0.5  # (3-7-2+4)/4 = -0.5

    assert statools.mean(a, b) == 1.25  # (-12+10+7+0)/4 = 1.25
    assert statools.mean(a, c) == -10.0 # (9-35-2-12)/4 = -10.0
    assert statools.mean(b, c) == -10.0 # (-12-14-14+0)/4 = -10.0

    assert statools.mean(a, a) == 11.0  # (9+25+1+9)/4 = 44/4 = 11.0
    assert statools.mean(b, b) == 17.25 # (16+4+49+0)/4 = 69/4 = 17.25
    assert statools.mean(c, c) == 19.5  # (9+49+4+16)/4 = 78/4 = 19.5

    assert statools.mean(a, b, c) == -30.0 # (-36-70-14+0)/4 = -30.0


def test_correlation(samples):
    x, y = samples
    assert statools.correlation(x, y) == pytest.approx(statistics.correlation(x, y))


def test_regression(samples):
    def linregress(a, b):
        result = stats.linregress(a, b)
        return result.slope, result.intercept

    x, y = samples
    assert statools.linear_regression(x, y) == pytest.approx(linregress(x, y))
    assert statools.linear_regression(y, x) == pytest.approx(linregress(y, x))
