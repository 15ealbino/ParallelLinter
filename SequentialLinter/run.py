# Sequential version
import glob
from sequentialLinter import run

# directory = input("Enter your directory: ")
lstOfFiles = []
lstOfFiles.append(
    "/Users/chrisjantzen/school/Fall2019/Parallel/finalProject/ParallelLinter/SequentialLinter/testFile.js"
)
for i in lstOfFiles:
    error = run(i)
    print(error)
