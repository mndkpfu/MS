import pytest
from random import randint, uniform

import pandas as pd
import scipy

from statools import *




def randata(a: float = 50, b: float = 100, ndigits: int = 1, minsize: int = 50, maxsize: int = 150) -> list[float]:
    return [round(uniform(a, b), ndigits) for _ in range(randint(minsize, maxsize))]


def test_statistics():
    data = randata()
    sdata = sorted(data)
    pdata = pd.Series(data)

    # Математическое ожидание
    assert mean(data) == pytest.approx(pdata.mean())

    # Дисперсия (смещенная и несмещенная) и стандартное отклонение
    assert variance(data) == pytest.approx(pdata.var(ddof=0))
    assert variance(data, unbiased=True) == pytest.approx(pdata.var())
    assert std(data) == pytest.approx(pdata.std(ddof=0))

    # Коэффициент ассиметрии
    assert skewness(data) == pytest.approx(scipy.stats.skew(pdata, bias=True))

    # Медиана и интерквартильная широта
    assert median(sdata) == pdata.median()
    assert iqr(sdata) == pdata.quantile(0.75, interpolation="midpoint") - pdata.quantile(0.25, interpolation="midpoint")