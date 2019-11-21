# Sequential version
import glob
from sequentialLinter import checkFile as run

directory = input("Enter your directory: ")
lstOfFiles = glob.glob(directory + "*.js")
for i in lstOfFiles:
    run(i)
