import matplotlib.pyplot as plt
import numpy as np


def plot_data(num_files, s_times, p_times):
    labels = [f"File {i}" for i in range(num_files)]
    xaxis = np.arange(num_files)
    width = 0.35

    fig, ax = plt.subplots(figsize=(10, 7))
    rects1 = ax.bar(
        xaxis - width / 2,
        [round(i, 4) for i in s_times],
        width,
        label="Sequential",
        color="#73d219",
    )
    rects2 = ax.bar(
        xaxis + width / 2,
        [round(i, 4) for i in p_times],
        width,
        label="Parallel",
        color="#3378f0",
    )

    ax.set_ylabel("Times")
    ax.set_title("Sequential vs. Parallel")
    ax.set_xticks(xaxis)
    ax.set_xticklabels(labels)
    ax.legend()

    def autolabel(rects):
        for rect in rects:
            height = rect.get_height()
            ax.annotate(
                "{}".format(height),
                xy=(rect.get_x() + rect.get_width() / 2, height),
                xytext=(0, 3),  # 3 points vertical offset
                textcoords="offset points",
                ha="center",
                va="bottom",
            )

    autolabel(rects1)
    autolabel(rects2)
    fig.tight_layout()

    plt.show()
