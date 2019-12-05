# Sequential version
import glob
from sequentialLinter import run as srun
from ParallelLinter import run as prun
from timeit import default_timer as timer
import matplotlib as plt


directory = input("Enter your directory: ")
lstOfFiles = glob.glob(directory + "*.js")
print("Sequential start")
startS = timer()
xaxis = []
yaxis = []
interations = 1
for i in lstOfFiles:
    result = srun(i)
    print(result)
    Sdone = timer() - startS

print("Parallel start")
startP = timer()
for i in lstOfFiles:
    startP = timer()
    result = prun(i)
    print(result)
    Pdone = timer() - startP
