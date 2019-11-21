#Sequential version
import sys
from sequentialLinter import checkFile as run
jsFile = sys.argv[0]

run(jsFile)