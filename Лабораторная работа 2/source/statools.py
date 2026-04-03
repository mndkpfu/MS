def mean(data: list[float]) -> float:
    return sum(data) / len(data)


def variance(data: list[float], unbiased: bool = False) -> float:
    if unbiased:
        return len(data) / (len(data) - 1) * variance(data, unbiased=False)
    return sum(x**2 for x in data) / len(data) - mean(data)**2