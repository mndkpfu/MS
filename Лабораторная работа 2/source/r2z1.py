""" Раздел 2. Задание 1

Проверить гипотезу о равенстве дисперсий по критерию Фишера, при
    α = 0.025
    K: σ 1-й группы меньше

При выбранной альтернативной гипотезе, значение критической константы и p-значение вычисляются как
    C = Ffish⁻¹(α | n-1, m-1)
    p = Ffish(f, n-1, m-1)
"""


from pathlib import Path
import logging

from scipy import stats

from tools import *
from statools import *




def main(path: str | Path):
    alpha = 0.025

    X, Y = read(path)
    n, m = len(X), len(Y)
    Xvar, Yvar = variance(X, unbiased=True), variance(Y, unbiased=True)
    F_stat = Xvar / Yvar
    logging.info(f"Исходные данные")
    logging.info(f"    Выборка X: {snippet(X)} ({n=})")
    logging.info(f"    Выборка Y: {snippet(Y)} ({m=})")
    logging.info(f"    Несмещенная дисперсия {Xvar=:.3f}")
    logging.info(f"    Несмещенная Дисперсия {Yvar=:.3f}")
    logging.info(f"    Статистика критерия Фишера {F_stat=:.3f}")

    # Проверка гипотезы через критическую константу
    C_crit = stats.f.ppf(alpha, n-1, m-1)
    logging.info(f"\nПроверка гипотезы через критическую константу")
    logging.info(f"    Критическая константа {C_crit=:.3f}")
    logging.info(f"    {F_stat=:.3f} {"<" if F_stat < C_crit else ">"} {C_crit=:.3f}")
    if F_stat < C_crit:
        logging.info("    Результат в критической области. H0 отвергается, верна H1: дисперсия 1-й группы меньше.")
    else:
        logging.info("    Результат вне критической области. Не достаточно обоснований отвергать H0.")

    # Проверка гипотезы через p-значение
    P_value = stats.f.cdf(F_stat, n-1, m-1)
    logging.info(f"\nПроверка гипотезы через p-значение")
    logging.info(f"    P-значение {P_value=:.3f}")
    logging.info(f"    {P_value=:.3f} {"<" if P_value < alpha else ">"} {alpha=:.3f}")
    if P_value < alpha:
        logging.info("    P-значение меньше уровня значимости. H0 отвергается, верна H1: дисперсия 1-й группы меньше.")
    else:
        logging.info("    P-значение не меньше уровня значимости. Не достаточно обоснований отвергать H0.")




if __name__ == "__main__":
    path = Path(__file__).parent.parent / "data/r2z1.csv"
    logging.basicConfig(level=logging.INFO, format="%(message)s")
    logging.info(__doc__)
    main(path)
