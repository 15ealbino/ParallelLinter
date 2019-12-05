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
iterations = 1
for i in lstOfFiles:
    result = srun(i)
    print(result)
    Sdone = timer() - startS
    sTimes.append(Sdone)
    iterations = iterations +1

print("Parallel start")
startP = timer()
for i in lstOfFiles:
    startP = timer()
    result = prun(i)
    print(result)
    Pdone = timer() - startP
    pTimes.append(Pdone)

xaxis = np.arange(0,iterations,1)
plt.plot(xaxis,sTimes,'r', label= "sequential" )
plt.plot (xaxis,pTimes,'b', label="parallel")
plt.xlabel('iterations')
plt.title('Parallel vs Sequential')
plt.ylabel('time')
plt.show()

