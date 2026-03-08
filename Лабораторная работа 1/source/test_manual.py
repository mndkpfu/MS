import pytest

from statools import *


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


def test_statistics():
    data = [15.0, 50.8, 12.2, 18.4, 25.3, 10.5, 30.7, 15.0, 22.1]
    sdata = [10.5, 12.2, 15.0, 15.0, 18.4, 22.1, 25.3, 30.7, 50.8]

    assert mean(data) == pytest.approx(22.22, abs=0.01)
    assert variance(data) == pytest.approx(139.43, abs=0.01)
    assert variance(data, unbiased=True) == pytest.approx(156.85, abs=0.01)
    assert std(data) == pytest.approx(11.81, abs=0.01)
    assert skewness(data) == pytest.approx(1.39, abs=0.01)
    assert median(sdata) == 18.4
    assert iqr(sdata) == 25.3 - 15.0