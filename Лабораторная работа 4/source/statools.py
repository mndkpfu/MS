from operator import mul
from itertools import starmap
from math import sqrt, prod
from typing import Iterable



def mean(*samples : list[float]):
    products = list(map(prod, zip(*samples)))
    return sum(products) / len(products)


def variance(data: list[float], unbiased: bool = False) -> float:
    if unbiased:
        return len(data) / (len(data) - 1) * variance(data, unbiased=False)
    return sum(x**2 for x in data) / len(data) - mean(data)**2


def correlation(x: list[float], y: list[float]) -> float:
    return (mean(list(starmap(mul, zip(x, y)))) - mean(x) * mean(y)) / sqrt(variance(x) * variance(y))


def linear_regression(x: list[float], y: list[float]) -> tuple[float, float]:
    # y = ax + b
    assert len(x) == len(y)
    a = (mean(x, y) - mean(x) * mean(y)) / (mean(x, x) - mean(x) * mean(x))
    b = mean(y) - a * mean(x)
    return a, b
