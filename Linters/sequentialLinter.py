def is_matched(expression):
    """
    >>> is_matched('test.js', '{}{}{()()}{([[]])}{[]}{[]}{()()}{}{}{}')
    test.js:
    'No Errors\\n'
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
                return_str += "Unopened {} on line {}\n".format(letter, line_number)
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
                        return_str += "There's a missing {0} for the {2} on line {1}\n".format(
                            i[0], i[1], rmapping[i[0]]
                        )
                else:
                    stack.reverse()
                    incorrect = stack.pop()
                    if stack:
                        stack.pop()
                    return_str += "Unopened {} on line {}\n".format(
                        incorrect[0], incorrect[1]
                    )
            else:
                stack.pop()
    if not stack and not return_str:
        return "No Errors\n"
    elif stack:
        for i in stack:
            return_str += "Unclosed {} on line {}\n".format(rmapping[i[0]], i[1])
        return "{}\n".format(return_str)
    else:
        return "{}\n".format(return_str)


def run(jsfile):
    s = ""
    print(f"{jsfile}:")
    with open(jsfile) as fp:
        line = fp.readline()
        s += line
        while line:
            line = fp.readline()
            s += line
    return is_matched(s)

