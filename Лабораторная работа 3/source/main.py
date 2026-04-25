""" Раздел 3. Задание 2.
Построить доверительные границы для дисперсии нормального распределения
    Q = 0.95 (соответственно α=0.05)
    Вид доверительной границы: двусторонняя
"""


from scipy import stats

from tools import *




def mean(data: list[float]) -> float:
    return sum(data) / len(data)


def variance(data: list[float], unbiased: bool = False) -> float:
    if unbiased:
        return len(data) / (len(data) - 1) * variance(data, unbiased=False)
    return sum(x**2 for x in data) / len(data) - mean(data)**2


def variance_interval(data: list[float], alpha: float) -> tuple[float, float]:
    n = len(data)
    df = n - 1
    s2 = variance(data, unbiased=False)

    lower = n * s2 / stats.chi2.ppf(1 - alpha / 2, df)
    upper = n * s2 / stats.chi2.ppf(alpha / 2, df)
    return lower, upper




if __name__ == "__main__":
    alpha = 0.05
    sample = read("r3z2.csv")

    print(__doc__)
    print(f"Исходные данные:\n    {snippet(sample)} (n={len(sample)})\n")

    lower, upper = variance_interval(sample, alpha)
    print(f"Доверительный интервал дисперсии (при α={alpha}): [{lower:.3f}, {upper:.3f}]")
    print(f"Дисперсия (смещенная): {variance(sample):.3f}")