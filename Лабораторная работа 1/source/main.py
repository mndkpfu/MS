from pathlib import Path

import matplotlib.pyplot

from statools import *
from plotools import *




def read(path: str | Path) -> list[float]:
    with open(path, "rt") as file:
        assert file.readline().strip() == '"X"'
        return list(map(float, file.readlines()))


def snippet(sample: list[float], head: int = 3, tail: int = 3) -> str:
    if head + tail >= len(sample):
        return repr(sample)
    first = repr(sample[:head]).removeprefix("[").removesuffix("]")
    last = repr(sample[-tail:]).removeprefix("[").removesuffix("]")
    return f"[{first}, ..., {last}]"


def descriptive_statistics(sample: list[float], ndigits: int = 2):
    statistics = (
        ("Объем выборки", len),
        ("Минимум", min),
        ("Максимум", max),
        ("Размах", lambda s: max(s) - min(s)),
        ("Математическое ожидание", mean),
        ("Выборочная дисперсия", variance),
        ("Выборочная дисперсия (несмещенная)", lambda s: variance(s, unbiased=True)),
        ("Стандартное отклонение", std),
        ("Коэффициент ассиметрии", skewness),
        ("Медиана", median),
        ("Интерквартильная широта", iqr)
    )

    for title, function in statistics:
        print(f"{title}: {round(function(sample), ndigits)}")


def show_plots(sample: list[float]):
    his_figure, his_axes = matplotlib.pyplot.subplots()
    histogram(sample, his_axes)
    his_axes.tick_params(axis="x", rotation=45)
    his_axes.set_title("Гистограмма")

    edf_figure, edf_axes = matplotlib.pyplot.subplots()
    edf_axes.tick_params(axis="x", rotation=45)
    edf(sample, edf_axes)
    edf_axes.set_title("ЭФР")

    # Стилизация ЭФР
    xticks = [quartile(sample, q) for q in range(5)]
    edf_axes.set_xticks(xticks)
    edf_axes.vlines(xticks, ymin=0, ymax=1, color="gray", linestyles="dashed", linewidth=0.8)

    matplotlib.pyplot.show()


def main(path: str | Path):
    sample = read(path)
    sample.sort()

    # Информация о выборке
    print(f"Файл: {path.resolve()}")
    print(f"Выборка: {snippet(sample)}")
    print()

    # Пункт 1. Характеристики выборки
    descriptive_statistics(sample)

    # Пункты 2 и 3. Гистограмма и ЭФР
    show_plots(sample)




if __name__ == "__main__":
    path = Path(__file__).resolve().parent / "../sample.csv"
    main(path)