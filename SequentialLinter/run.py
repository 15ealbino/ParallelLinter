# Sequential version
import glob
from sequentialLinter import run


directory = input("Enter your directory: ")
lstOfFiles = glob.glob(directory + "*.js")
for i in lstOfFiles:
    result = run(i)
    print(result)
