# based on https://www.geeksforgeeks.org/check-for-balanced-parentheses-in-python/


def is_matched(expression):
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
    queue = []
    line_number = 1
    return_str = ""

    for letter in expression:
        if letter is "\n":
            line_number += 1
        if letter in opening:
            queue.append((mapping[letter], line_number))
        elif letter in closing:
            if not queue:
                return_str += "Unopened closing {} on line {}".format(
                    letter, line_number
                )
            elif letter != queue[-1][0]:
                popped = queue.pop()
                return_str += "There's a missing {} on line {}\n".format(
                    popped[0], popped[1]
                )
            else:
                queue.pop()
    if not queue and not return_str:
        return "All good"
    else:
        return return_str


def run(jsfile):
    s = ""
    with open(jsfile) as fp:
        line = fp.readline()
        s += line
        while line:
            line = fp.readline()
            s += line
    return is_matched(s)

