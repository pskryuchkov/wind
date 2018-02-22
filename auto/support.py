from pprint import pprint
import re
from numpy import *
from pathlib import Path
import matplotlib.pyplot as plt

fields_names = ["time",
                "pr_force_x",
                "pr_force_y",
                "pr_force_z",
                "vi_force_x",
                "vi_force_y",
                "vi_force_z",
                "po_force_x",
                "po_force_y",
                "po_force_z",
                "pr_moment_x",
                "pr_moment_y",
                "pr_moment_z",
                "vi_moment_x",
                "vi_moment_y",
                "vi_moment_z",
                "po_moment_x",
                "po_moment_y",
                "po_moment_z",
                ]


def load_forces(fn):
    with open(fn, "r") as f:
        text = f.readlines()

    raw_data = []
    for line in text:
        if "#" in line:
            continue

        s = line.replace("(", "")
        s = s.replace(")", "")
        s = s.replace("\t", "")
        raw_data.append(list(zip(fields_names, list(map(float, s.split())))))

    data = {}
    for j, x in enumerate(fields_names):
        vals = []
        for line in raw_data:
            vals.append(line[j][1])
        data[x] = array(vals)

    return data


def draw_shape(fn, c="blue"):
    with open(fn) as f:
        text = f.readlines()

    data = array([list(map(float, line.split())) for line in text])
    xc, yc = data[:, 0], data[:, 1]

    wide = 7
    xs, ys = -1.0, -3.0

    plt.figure(figsize=(9, 6))
    plt.xlim([xs, xs + wide])
    plt.ylim([ys, ys + wide])

    for yp in list(set(yc)):
        plt.axhline(yp, c="grey", lw=0.2, alpha=0.7)

    for xp in list(set(xc)):
        plt.axvline(xp, c="grey", lw=0.2, alpha=0.7)

    plt.title(Path(fn).stem, style='italic')
    plt.plot(xc, yc, "o", markeredgewidth=0.0, c=c)