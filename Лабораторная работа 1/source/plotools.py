from itertools import pairwise, chain

from matplotlib.axes import Axes
import matplotlib.patches as patches
from matplotlib import colormaps




def histogram(data: list[float], axes: Axes, pallete: str = "viridis"):
    number = len(data) // 10
    width = (max(data) - min(data)) / (number - 1)
    edges = list((min(data) - width/2 + width*i) for i in range(number + 1))
    heights = list(sum(left < x <= right for x in data) / (len(data) * width) for left, right in pairwise(edges))

    cmap = colormaps.get_cmap(pallete)
    for i, ((left, right), height) in enumerate(zip(pairwise(edges), heights)):
        rect = patches.Rectangle((left, 0), width, height, facecolor=cmap(i / number))
        axes.add_patch(rect)
    axes.set_xticks(edges)
    axes.set_yticks(heights)
    axes.autoscale_view()


def edf(data: list[float], axes: Axes, delta: float = 5):
    steps, heights = [data[0] - delta], [0]
    for x in data:
        if x == steps[-1]:
            heights[-1] += 1
        else:
            heights.append(heights[-1] + 1)
            steps.append(x)
    steps.append(data[-1] + delta)
    #heights.append(len(data))
    heights = [x / len(data) for x in heights]

    for (left, right), height in zip(pairwise(steps), heights):
        axes.plot([left, right], [height, height])

    axes.set_yticks(list(chain([0, 1], *max_diffs(heights))))
    axes.set_xticks(list(chain([data[0], data[-1]], *max_diffs(steps[1:-1]))))



def max_diffs(data: list[float], n: int = 3) -> list[float]:
    diffs = sorted(pairwise(data), key=lambda x: abs(x[0] - x[1]), reverse=True)
    return diffs[:n]