""" Раздел 4. Задание 2
Построить прогноз (регрессию) X по значению Y при Y = 79
"""

from matplotlib.axes import Axes
import matplotlib.pyplot as plt

from tools import *
from statools import *




X, Y = read("r4z2.csv", ["X", "Y"])
print(__doc__)


# Информация о выборках и регрессия
print(f"Выборочный коэффициент корреляции: {correlation(X, Y)}\n")

a, b = linear_regression(Y, X)
print(f"Уравнение линейной регрессии: x = {a:.2f}y + {b:.2f}\n")

y_target = 79
x_pred = a * y_target + b
print(f"По y={y_target} спрогнозировано x={x_pred:.3f}\n")


# График
dy = 1
plt.xlabel("Независимая выборка Y")
plt.ylabel("Зависимая выборка X")
# plt.title("Линейная регрессия X по Y")

plt.plot(Y, X, ".",)

y_min, y_max = min(Y) - dy, max(Y) + dy
plt.plot([y_min, y_max], [a * y_min + b, a * y_max + b], "r-",)

ax = plt.gca()
x_lims = ax.get_xlim()
y_lims = ax.get_ylim()

plt.plot([y_target, y_target], [y_lims[0], x_pred], "g--", alpha=0.6, linewidth=1.2)
plt.plot([x_lims[0], y_target], [x_pred, x_pred], "g--", alpha=0.6, linewidth=1.2)
plt.plot(y_target, x_pred, "go", markersize=5, zorder=5)

ax.set_xlim(x_lims)
ax.set_ylim(y_lims)

current_xticks = list(ax.get_xticks())
current_yticks = list(ax.get_yticks())

plt.xticks(current_xticks + [y_target])
plt.yticks(current_yticks + [x_pred], [f"{tick:.1f}" for tick in current_yticks] + [f"{x_pred:.1f}"])

plt.grid(True, linestyle=":", alpha=0.5)
plt.show()
