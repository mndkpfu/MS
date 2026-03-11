from itertools import pairwise

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
