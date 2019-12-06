# Sequential version
import glob
from sequentialLinter import run as srun
from ParallelLinter import run as prun
from plotData import plot_data
from timeit import default_timer as timer


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

plot_data(len(lstOfFiles), sTimes, pTimes)
