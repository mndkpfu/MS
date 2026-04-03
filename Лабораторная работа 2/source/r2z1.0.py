""" Раздел 2. Задание 1.0

Проверить гипотезу об однородности (равенстве средних) по одновыборочному критерию Стьюдента (двухвыборочный вариант), при
    α = 0.025
    K: Изменится (μ₁≠μ₂)

При выбранной альтернативной гипотезе, значение критической константы и p-значение вычисляются как
    C = Fstud⁻¹(1-α/2 | n-1)
    p = 2(1-Fstud(|t| | n-1))
"""


from pathlib import Path
import logging
import math

from scipy import stats

from tools import *
from statools import *




def t_stat(data: list[float], m0: float) -> float:
    return (mean(data) - m0) / std(data, unbiased=False) * math.sqrt(len(data) - 1)


def main(path: Path | str):
    alpha = 0.025

    X, Y = read(path)
    assert len(X) == len(Y)
    U = [x - y for x, y in zip(X, Y)]
    T_stat = t_stat(U, 0)
    logging.info("Исходные данные")
    logging.info(f"    Выборка X: {snippet(X)} (n={len(X)})")
    logging.info(f"    Выборка Y: {snippet(Y)} (n={len(Y)})")
    logging.info(f"    Разность U: {snippet(U)}")
    logging.info(f"    Статистика Стьюдента для разности: {T_stat=:.3f}")

    # Проверка гипотезы через критическую константу (отвергается, если |T| > C)
    C_crit = stats.t.ppf(1-alpha/2, df=len(U)-1)
    logging.info(f"\nПроверка гипотезы через критическую константу")
    logging.info(f"    Критическая константа {C_crit=:.3f}")
    logging.info(f"    {abs(T_stat)=:.3f} {"<" if abs(T_stat) < C_crit else ">"} {C_crit=:.3f}")
    if abs(T_stat) > C_crit:
        logging.info("    Результат в критической области. H0 отвергается, верна H1.")
    else:
        logging.info("    Результат вне критической области. Не достаточно обоснований отвергать H0.")

    # Проверка через p-значение (отвергается, если p < α)
    P_value = 2 * (1-stats.t.cdf(abs(T_stat), df=len(U)-1))
    logging.info(f"\nПроверка гипотезы через p-значение")
    logging.info(f"    P-значение {P_value=:.3f}")
    logging.info(f"    {P_value=:.3f} {"<" if P_value < alpha else ">"} {alpha=:.3f}")
    if P_value < alpha:
        logging.info("    P-значение меньше уровня значимости. H0 отвергается, верна H1.")
    else:
        logging.info("    P-значение не меньше уровня значимости. Не достаточно обоснований отвергать H0.")




if __name__ == "__main__":
    path = Path(__file__).parent.parent / "data/r2z1.0.csv"
    logging.basicConfig(level=logging.INFO, format="%(message)s")
    logging.info(__doc__)
    main(path)
