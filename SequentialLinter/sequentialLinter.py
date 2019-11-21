# based on https://www.geeksforgeeks.org/check-for-balanced-parentheses-in-python/


def checkFile(jsFile):
    open_list = ["[", "{", "("]
    close_list = ["]", "}", ")"]

    newLineCount = 0
    stack = []
    for i in jsFile:
        if i == "\n":
            newLineCount += 1
        if i in open_list:
            stack.append(i)
        elif i in close_list:
            pos = close_list.index(i)
            if (len(stack) > 0) and (open_list[pos] == stack[len(stack) - 1]):
                stack.pop()
            else:
                return "Unbalanced at line {}".format(newLineCount)
    if len(stack) == 0:
        return "File is all good"


def run(jsfile):
    s = ""
    with open(jsfile) as fp:
        line = fp.readline()
        s += line
        while line:
            line = fp.readline()
            s += line
    return checkFile(s)

