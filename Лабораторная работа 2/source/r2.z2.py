""" Раздел 2. Задание 2

Проверить гипотезу о том, что распределение совпадает с экспоненциальным распределением E(λ = 2), при
    α = 0.01
"""


from pathlib import Path
import logging
import math
from typing import Callable

from scipy import stats
import matplotlib.pyplot as plt

from tools import *
from statools import *




def d_stat(data: list[float], F: Callable) -> float:
    # Для ЭФР непрерывной слева
    return max(abs(sum(y <= x for y in data) / len(data) - F(x)) for x in data)


def main(path: str | Path):
    alpha = 0.01
    l = 2
    F = lambda x: 1 - math.exp(-l * x)

    X = read(path)
    n = len(X)
    D_stat = d_stat(X, F)
    K_stat = math.sqrt(len(X)) * D_stat
    logging.info(f"Исходные данные")
    logging.info(f"    Выборка X: {snippet(X, ndigits=8)} (n={len(X)})")
    logging.info(f"    D-статистика (sup) {D_stat=:.3f}")
    logging.info(f"    K-статистика (sqrt) {K_stat=:.3f}")

    # Проверка гипотезы через критическую константу (отвергается, если K > C)
    C_crit = math.sqrt(-0.5 * math.log(alpha / 2))
    logging.info(f"\nПроверка гипотезы через критическую константу")
    logging.info(f"    Критическая константа (аппроксимация) {C_crit=:.3f}")
    logging.info(f"    Критическая константа (из распределения): {stats.kstwobign.ppf(1 - alpha):.3f}")
    logging.info(f"    {K_stat=:.3f} {"<" if K_stat < C_crit else ">"} {C_crit=:.3f}")
    if K_stat > C_crit:
        logging.info("    Результат в критической области. H0 отвергается: данные не соответствуют E(λ=2).")
    else:
        logging.info("    Результат вне критической области. Не достаточно обоснования отвергнуть H0: данные соответствуют E(λ=2).")

    # Проверка гипотезы через p-значение
    P_value = 2 * math.exp(-2 * (K_stat**2))
    logging.info(f"\nПроверка гипотезы через p-значение")
    logging.info(f"    P-значение (аппроксимация) {P_value=:.3f}")
    logging.info(f"    P-значение (из распределения) {stats.kstwobign.sf(K_stat):.3f}")
    logging.info(f"    {P_value=:.3f} {"<" if P_value < alpha else ">"} {alpha=:.3f}")
    if P_value < alpha:
        logging.info("    P-значение меньше уровня значимости. H0 отвергается, верна H1.")
    else:
        logging.info("    P-значение не меньше уровня значимости. Не достаточно обоснований отвергать H0.")

    # Визуализация
    plot_distributions(X)


def plot_distributions(data: list[float], l: float = 2):
    x_sorted = sorted(data)
    n = len(x_sorted)

    x_step = [0]
    y_step = [0]

    for i, x in enumerate(x_sorted):
        x_step.append(x)
        y_step.append(i / n)
        x_step.append(x)
        y_step.append((i + 1) / n)

    x_step.append(max(x_sorted) + 0.5)
    y_step.append(1.0)

    max_x = max(x_sorted) + 0.5
    steps = 100
    x_theory = [max_x * i / steps for i in range(steps + 1)]
    y_theory = [1 - math.exp(-l * x) for x in x_theory]

    plt.figure(figsize=(10, 6))

    plt.plot(x_step, y_step, label="ЭФР", color="blue", linewidth=2)
    plt.plot(x_theory, y_theory, label=rf"$E(\lambda={l})$", color="red", linestyle="--")

    plt.legend()
    plt.grid(True, linestyle=':', alpha=0.7)
    plt.show()




if __name__ == "__main__":
    path = Path(__file__).parent.parent / "data/r2z2.csv"
    logging.basicConfig(level=logging.INFO, format="%(message)s")
    logging.info(__doc__)
    main(path)