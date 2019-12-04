# Based on https://codereview.stackexchange.com/questions/180567/checking-for-balanced-brackets-in-python


def is_matched(file_name, expression):
    """
    >>> is_matched('test.js', '{}{}{()()}{([[]])}{[]}{[]}{()()}{}{}{}')
    test.js:
    'All good\\n'
    """
    opening = tuple("({[")
    closing = tuple(")}]")
    mapping = dict(zip(opening, closing))
    rmapping = dict(zip(closing, opening))
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
                return_str += "Unopened closing {} on line {}\n".format(
                    letter, line_number
                )
            elif letter != stack[-1][0]:
                popped = []
                temp = [x for x in stack]
                stack.reverse()
                found_pair = False
                for i in stack:
                    if i[0] == letter:
                        found_pair = True
                if found_pair:
                    for i in stack:
                        if i[0] != letter:
                            popped.append(temp.pop())
                        else:
                            temp.pop()
                            break
                    temp.reverse()
                    stack = temp
                    popped.reverse()
                    for i in popped:
                        return_str += "There's a missing {} on line {}\n".format(
                            i[0], i[1]
                        )
                else:
                    stack.reverse()
                    incorrect = stack.pop()
                    if stack:
                        stack.pop()
                    return_str += "There's an extra closing {} on line {}\n".format(
                        incorrect[0], incorrect[1]
                    )
            else:
                stack.pop()
    print("{}:".format(file_name))
    if not stack and not return_str:
        return "All good\n"
    elif stack:
        for i in stack:
            return_str += "Unclosed {} on line {}\n".format(rmapping[i[0]], i[1])
        return "{}\n".format(return_str)
    else:
        return "{}\n".format(return_str)


# print(is_matched("ts", "]\n[()(]\n[("))


def run(jsfile):
    s = ""
    with open(jsfile) as fp:
        line = fp.readline()
        s += line
        while line:
            line = fp.readline()
            s += line
    return is_matched(jsfile, s)

