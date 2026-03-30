def edf(data: list[float]) -> dict[float, float]:
    heights = {x: sum(y < x for y in data) for x in sorted(data)}
    return heights
