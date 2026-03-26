""" Раздел 2. Задание 1.0
Проверить гипотезу об однородности по одновыборочному критерию Стьюдента (двухвыборочный вариант), при
    α = 0.025
    K: Изменится

При выбранной альтернативной гипотезе, значение критической константы и p-значение вычисляются как
    C = Fstud⁻¹(1-α/2 | n-1)
    p = 2(1-Fstud(|t| | n-1))
"""


from pathlib import Path
import logging
import math
import statistics

from scipy import stats
import matplotlib.pyplot as plt

from tools import *





def t_stat(data: list[float], m0: float) -> float:
    # pstdev - смещенная дисперсия (stdev - несмещенная)
    return (statistics.mean(data) - m0) / statistics.pstdev(data) * math.sqrt(len(data) - 1)


def c_crit(alpha: float, n: int) -> float:
    return stats.t.ppf(1-alpha/2, df=n-1)


def p_value(t: float, n: int) -> float:
    return 2*(1-stats.t.cdf(abs(t), df=n-1))


def graph(C: float, T: float, n: int, title: str = ""):
    MIN, MAX = -5, 5

    xs = linspace(MIN, MAX, 200)
    ys = stats.t.pdf(xs, n-1)

    x_crit_left = linspace(MIN, -C, 100)
    x_crit_right = linspace(C, MAX, 100)

    plt.plot(xs, ys)

    plt.fill_between(xs, ys, color="blue", alpha=0.1)
    plt.fill_between(x_crit_left, stats.t.pdf(x_crit_left, n-1), color="red", alpha=0.3)
    plt.fill_between(x_crit_right, stats.t.pdf(x_crit_right, n-1), color="red", alpha=0.3)

    plt.axvline(T, color="green", alpha=0.4, linestyle='--', linewidth=2)

    plt.xticks([round(x, 2) for x in (-C, C, T)])
    plt.grid(True, linestyle='--', alpha=0.6)
    plt.title(title)

    plt.show()



def main(path: Path | str):
    alpha = 0.025

    X, Y = read(path)
    logging.info(f"Выборка X: {snippet(X)} (n={len(X)})")
    logging.info(f"Выборка Y: {snippet(Y)} (n={len(Y)})")

    U = [x - y for x, y in zip(X, Y)]
    logging.info(f"Разность U: {snippet(U)}")

    T = t_stat(U, 0)
    logging.info(f"T-статистика разности: {round(T, 3)}")

    C = c_crit(alpha, len(U))
    P = p_value(T, len(U))
    logging.info(f"Критическая константа: {round(C, 3)}")
    logging.info(f"P-значение: {round(P, 3)}")

    if abs(T) > C:
        logging.info("Результат в критической области. Нулевую гипотезу следует отвергнуть.")
    else:
        logging.info("Результат вне критической области. Нулевую гипотезу следует принять.")

    graph(C, T, len(U), title=f"Критерий Стьюдента")




if __name__ == "__main__":
    path = Path(__file__).parent.parent / "data/r2z1.0.csv"
    logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")
    main(path)