# Sequential version
import glob
from sequentialLinter import run

directory = input("Enter your directory: ")
lstOfFiles = glob.glob(directory + "*.js")
for i in lstOfFiles:
    error = run(i)
    if(error == "File is all good"):
        print(i + " has no errors")
    else:
        print("The file " + i + " has the following errors: " + "\n" + error)
    
