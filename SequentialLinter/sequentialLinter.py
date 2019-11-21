# https://www.geeksforgeeks.org/check-for-balanced-parentheses-in-python/


def checkFile(jsFile):
    open_list = ["[", "{", "("]
    close_list = ["]", "}", ")"]

    with open(jsFile) as fp:
        line = fp.readline()
        cnt = 1
        stack = []
        while line:
            print("Line {}: {}".format(cnt, line.strip()))
            line = fp.readline()
            cnt += 1
            for i in line:
                if i in open_list:
                    stack.append(i)
                elif i in close_list:
                    pos = close_list.index(i)
                if (len(stack) > 0) and (open_list[pos] == stack[len(stack) - 1]):
                    stack.pop()
                else:
                    return ("Unbalanced at line ", cnt)
        if len(stack) == 0:
            return "File is all good"
