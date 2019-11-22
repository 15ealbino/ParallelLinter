# based on https://www.geeksforgeeks.org/check-for-balanced-parentheses-in-python/


def checkFile(jsFile):
    open_list = ["[", "{", "("]
    close_list = ["]", "}", ")"]

    newLineCount = 1
    stack = []
    returnStr = ""
    for i in jsFile:
        if i == "\n":
            newLineCount += 1
        if i in open_list:
            stack.append([i,newLineCount])
        elif i in close_list:
            pos = close_list.index(i)
            if (len(stack) > 0) and (open_list[pos] == stack[len(stack) - 1][0]):
                stack.pop()
            else:
                if len(stack) == 0:
                    returnStr += "Extra close " + i + "on line " + str(newLineCount)
                else:
                    for j in stack:
                        error = "The " + j[0] + " on line " + str(j[1]) +  " is not closed \n"
                        returnStr += error
    if len(stack) == 0 and returnStr == "":
        returnStr =  "File is all good"
    return returnStr

def run(jsfile):
    s = ""
    with open(jsfile) as fp:
        line = fp.readline()
        s += line
        while line:
            line = fp.readline()
            s += line
    return checkFile(s)

