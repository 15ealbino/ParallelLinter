# Sequential version
import glob
from sequentialLinter import run as srun
from ParallelLinter import run as prun
from timeit import default_timer as timer
import matplotlib.pyplot as plt
import numpy as np


directory = input("Enter your directory: ")
lstOfFiles = glob.glob(directory + "*.js")
print("Sequential start")
startS = timer()
pTimes = []
sTimes = []
for i in lstOfFiles:
    result = srun(i)
    print(result)
    Sdone = timer() - startS
    sTimes.append(Sdone)

print("Parallel start")
startP = timer()
for i in lstOfFiles:
    startP = timer()
    result = prun(i)
    print(result)
    Pdone = timer() - startP
    pTimes.append(Pdone)


labels = [f"File {i}" for i in range(len(lstOfFiles))]
xaxis = np.arange(len(lstOfFiles))
width = 0.35

fig, ax = plt.subplots(figsize=(10, 7))
rects1 = ax.bar(
    xaxis - width / 2,
    [round(i, 4) for i in sTimes],
    width,
    label="Sequential",
    color="#73d219",
)
rects2 = ax.bar(
    xaxis + width / 2,
    [round(i, 4) for i in pTimes],
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
