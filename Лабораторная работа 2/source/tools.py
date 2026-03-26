from pathlib import Path
import csv


__all__ = ["read", "snippet", "linspace"]


def read(path: Path | str, titles: None | list[str] = None) -> tuple[list[float]]:
    with open(path, "rt") as file:
        reader = csv.reader(file)
        assert next(reader) == titles or titles is None
        columns = tuple(list(map(float, filter(bool, column))) for column in zip(*reader))
        return columns[0] if len(columns) == 1 else columns


def snippet(sample: list[float], head: int = 3, tail: int = 3, ndigits: int = 1) -> str:
    if head + tail >= len(sample):
        return repr(sample)
    first = repr([round(x, ndigits) for x in sample[:head]]).removeprefix("[").removesuffix("]")
    last = repr([round(x, ndigits) for x in sample[-tail:]]).removeprefix("[").removesuffix("]")
    return f"[{first}, ..., {last}]"


def linspace(start: float, stop: float, num: float) -> list[float]:
    assert num > 2
    step = (stop - start) / (num - 1)
    return [start + i * step for i in range(num)]