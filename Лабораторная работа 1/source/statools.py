def mean(data: list[float]) -> float:
    return sum(data) / len(data)


def variance(data: list[float], unbiased: bool = False) -> float:
    if unbiased:
        return len(data) / (len(data) - 1) * variance(data, unbiased=False)
    return sum(x**2 for x in data) / len(data) - mean(data)**2


def quartile(data: list[float], q: int) -> float:
    n = len(data)
    index = (n - 1) * q / 4
    if index.is_integer():
        return data[int(index)]
    return (data[int(index)] + data[int(index) + 1]) / 2


def median(data: list[float]) -> float:
    return quartile(data, 2)


def iqr(data: list[float]) -> float:
    return quartile(data, 3) - quartile(data, 1)