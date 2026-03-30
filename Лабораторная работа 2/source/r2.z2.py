""" Раздел 2. Задание 2
Проверить гипотезу о том, что распределение совпадает с экспоненциальным распределением E(λ = 2), при
    α = 0.01


"""


from pathlib import Path
import logging
import math
import statistics
from typing import Callable

from scipy import stats
import matplotlib.pyplot as plt

from tools import *
from statools import *




def d_stat(data: list[float], F: Callable) -> float:
    # Для ЭФР непрерывной слева
    return max(abs(sum(y <= x for y in data) / len(data) - F(x)) for x in data)


def main(path: str | Path):
    l = 2
    alpha = 0.01
    F = lambda x: 1 - math.exp(-l * x)

    X = read(path)
    logging.info(f"Выборка X: {snippet(X, ndigits=8)} (n={len(X)})")

    D = d_stat(X, F)
    logging.info(f"D-статистика (sup) для показательного распределения: {D}")

    K = math.sqrt(len(X)) * D
    logging.info(f"K-статистика (sqrt)")

    C = math.sqrt(-0.5 * math.log(alpha / 2))
    logging.info(f"Критическая константа: {C}")

    P = 2 * math.exp(-2 * (K**2))
    logging.info(f"P-значение: {P}")

    if K > C:
        logging.info("Результат в критической области. Нулевую гипотезу следует отвергнуть.")
    else:
        logging.info("Результат вне критической области. Нулевую гипотезу следует принять.")
    logging.info(f"{P=:.4f} {"<" if (alpha>P) else ">"} {alpha=:.4f}, гипотеза {"отвергается" if P < alpha else "принимается"}")




if __name__ == "__main__":
    path = Path(__file__).parent.parent / "data/r2z2.csv"
    logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")
    main(path)