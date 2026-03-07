import pytest
from random import randint, uniform

import pandas as pd
import scipy

from statools import *




def randata(a: float = 50, b: float = 100, ndigits: int = 1, minsize: int = 50, maxsize: int = 150) -> list[float]:
    return [round(uniform(a, b), ndigits) for _ in range(randint(minsize, maxsize))]


def test_mean():
    for _ in range(50):
        data = randata()
        assert mean(data) == pytest.approx(pd.Series(data).mean())


def test_variance():
    for _ in range(50):
        data = randata()
        assert variance(data, unbiased=False) == pytest.approx(pd.Series(data).var(ddof=0))

    for _ in range(50):
        data = randata()
        assert variance(data, unbiased=True) == pytest.approx(pd.Series(data).var())


def test_std():
    for _ in range(50):
        data = randata()
        assert std(data) == pytest.approx(pd.Series(data).std(ddof=0))


def test_skewness():
    for _ in range(50):
        data = randata()
        assert skewness(data) == pytest.approx(scipy.stats.skew(pd.Series(data), bias=True))


def test_quartile_length():
    # n=5 (n-1)=4
    # q=1 (1/4):  (n-1)q=1  [(n-1)q]=1  data[1]
    # q=2 (2/4):  (n-1)q=2  [(n-1)q]=2  data[2]
    # q=3 (3/4):  (n-1)q=3  [(n-1)q]=3  data[3]
    data5 = [0, 1, 2, 3, 4]
    assert quartile(data5, 0) == 0
    assert quartile(data5, 1) == 1
    assert quartile(data5, 2) == 2
    assert quartile(data5, 3) == 3
    assert quartile(data5, 4) == 4

    # n=6 (n-1)=5
    # q=1 (1/4):  (n-1)q=1.25  [(n-1)q]=1  (data[1]+data[2])/2
    # q=2 (2/4):  (n-1)q=2.5   [(n-1)q]=2  (data[2]+data[3])/2
    # q=3 (3/4):  (n-1)q=3.75  [(n-1)q]=3  (data[3]+data[4])/2
    data6 = [0, 1, 2, 3, 4, 5]
    assert quartile(data6, 0) == 0
    assert quartile(data6, 1) == 1.5
    assert quartile(data6, 2) == 2.5
    assert quartile(data6, 3) == 3.5
    assert quartile(data6, 4) == 5

    # n=7 (n-1)=6
    # q=1 (1/4):  (n-1)q=1.5  [(n-1)q]=1  (data[1]+data[2])/2
    # q=2 (2/4):  (n-1)q=3    [(n-1)q]=3  data[3]
    # q=3 (3/4):  (n-1)q=4.5  [(n-1)q]=4  (data[4]+data[5])/2
    data7 = [0, 1, 2, 3, 4, 5, 6]
    assert quartile(data7, 0) == 0
    assert quartile(data7, 1) == 1.5
    assert quartile(data7, 2) == 3
    assert quartile(data7, 3) == 4.5
    assert quartile(data7, 4) == 6

    # n=8 (n-1)=7
    # q=1 (1/4):  (n-1)q=1.75  [(n-1)q]=1  (data[1]+data[2])/2
    # q=2 (2/4):  (n-1)q=3.5   [(n-1)q]=3  (data[3]+data[4])/2
    # q=3 (3/4):  (n-1)q=5.25  [(n-1)q]=5  (data[5]+data[6])/2
    data8 = [0, 1, 2, 3, 4, 5, 6, 7]
    assert quartile(data8, 0) == 0
    assert quartile(data8, 1) == 1.5
    assert quartile(data8, 2) == 3.5
    assert quartile(data8, 3) == 5.5
    assert quartile(data8, 4) == 7

    # n=42 (n-1)=41
    # q=1 (1/4):  (n-1)q=10.25  [(n-1)q]=10  (data[10]+data[11])/2
    # q=2 (2/4):  (n-1)q=20.5   [(n-1)q]=20  (data[20]+data[21])/2
    # q=3 (3/4):  (n-1)q=30.75  [(n-1)q]=30  (data[30]+data[31])/2
    data42 = list(range(42))
    assert quartile(data42, 0) == 0
    assert quartile(data42, 1) == 10.5
    assert quartile(data42, 2) == 20.5
    assert quartile(data42, 3) == 30.5
    assert quartile(data42, 4) == 41

    # n=89 (n-1)=88
    # q=1 (1/4):  (n-1)q=22  [(n-1)q]=22  data[22]
    # q=2 (2/4):  (n-1)q=44  [(n-1)q]=22  data[44]
    # q=3 (3/4):  (n-1)q=66  [(n-1)q]=22  data[66]
    data89 = list(range(89))
    assert quartile(data89, 0) == 0
    assert quartile(data89, 1) == 22
    assert quartile(data89, 2) == 44
    assert quartile(data89, 3) == 66
    assert quartile(data89, 4) == 88


def test_median():
    for _ in range(50):
        data = randata()
        assert median(sorted(data)) == pd.Series(data).median()


def test_iqr():
    pandas_iqr = lambda s: s.quantile(0.75, interpolation='midpoint') - s.quantile(0.25, interpolation='midpoint')
    for _  in range(50):
        data = randata()
        assert iqr(sorted(data)) == pandas_iqr(pd.Series(data))
