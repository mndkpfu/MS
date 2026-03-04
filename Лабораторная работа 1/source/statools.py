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