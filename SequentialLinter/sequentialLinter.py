# Based on https://codereview.stackexchange.com/questions/180567/checking-for-balanced-brackets-in-python


def is_matched(file_name, expression):
    """
    Finds out how balanced an expression is.
    With a string containing only brackets.

    >>> is_matched('[]()()(((([])))')
    False
    >>> is_matched('[](){{{[]}}}')
    True
    """
    opening = tuple("({[")
    closing = tuple(")}]")
    mapping = dict(zip(opening, closing))
    stack = []
    line_number = 1
    return_str = ""

    for letter in expression:
        if letter is "\n":
            line_number += 1
        elif letter in opening:
            stack.append((mapping[letter], line_number))
        elif letter in closing:
            if not stack:
                return_str += "Unopened closing {} on line {}".format(
                    letter, line_number
                )
            elif letter != stack[-1][0]:
                popped = []
                stack.reverse()
                temp = [x for x in stack]
                temp.reverse()
                for i in stack:
                    if i[0] != letter:
                        popped.append(temp.pop())
                temp.reverse()
                stack = [x for x in temp]
                popped.reverse()
                for i in popped:
                    return_str += "There's a missing {} on line {}\n".format(i[0], i[1])
            else:
                stack.pop()
    print("{}:".format(file_name))
    if not stack and not return_str:
        return "All good\n"
    elif stack:
        for i in stack:
            return_str += "Unclosed {} on line {}\n".format(i[0], i[1])
        return "{}\n".format(return_str)
    else:
        return "{}\n".format(return_str)


def run(jsfile):
    s = ""
    with open(jsfile) as fp:
        line = fp.readline()
        s += line
        while line:
            line = fp.readline()
            s += line
    return is_matched(jsfile, s)

