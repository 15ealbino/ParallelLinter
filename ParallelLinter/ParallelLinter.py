# parallel linter
import multiprocessing as mp
import math

"""
___ ___ ___ ___
 \  /    \   /
  --      --
   \      /
    ------

Go through and break up the expression in 4 - x number of pieces based on the size of the file
If there is a problem, return fail right away and have that be appended to the global list of sets.
    if not broken, just append an empty list to the global set of lists and if one is an empty list, just ignore that run immediately.
broken_up_sets[i:i+2] where i += 2 after each new call to is_matched with new sets, keep this until i+2 > len(broken_up_sets)
create new function for getting specifics of problems when len(broken_up_sets) == 1
"""


def split_expression(expression, num_splits=4):
    n = math.ceil(len(expression) / num_splits)
    return [expression[i : i + n] for i in range(0, len(expression), n)]


def is_matched(expression):
    opening = tuple("({[")
    closing = tuple(")}]")
    mapping = dict(zip(opening, closing))
    stack = []
    return_str = ""

    for character in expression:
        if character[0] in opening:
            stack.append([mapping[character[0]], character[1]])
        elif character[0] in closing:
            if not stack:
                return_str += "Unopened closing {} on line {}".format(
                    character[0], character[1]
                )
            elif character[0] != stack[-1][0]:
                popped = []
                for i in stack:
                    if i[0] != character[0]:
                        popped.append(stack.pop())
                    else:
                        stack.pop()
                        break
                popped.reverse()
                for i in popped:
                    return_str += "There's a missing {} on line {}\n".format(i[0], i[1])
            else:
                stack.pop()
    if not stack and not return_str:
        return "All good\n"
    elif stack:
        for i in stack:
            return_str += "Unclosed {} on line {}\n".format(i[0], i[1])
        return "{}\n".format(return_str)
    else:
        return "{}\n".format(return_str)


def get_unmatched(expression):
    """
    Returns a list of values that weren't paired in the order of when they occured.
    """
    opening = tuple("({[")
    closing = tuple(")}]")
    mapping = dict(zip(opening, closing))
    rmapping = dict(zip(closing, opening))
    stack = []
    line_number = 1
    incorrects = []

    for letter in expression:
        if letter is "\n":
            line_number += 1
        elif letter in opening:
            stack.append([mapping[letter], line_number])
        elif letter in closing:
            if not stack:
                incorrects.append([letter, line_number])

            elif letter != stack[-1][0]:
                popped = []
                for i in stack:
                    if i[0] != letter:
                        popped.append(stack.pop())
                    else:
                        stack.pop()
                        break
                popped.reverse()
                for i in popped:
                    incorrects.append([rmapping[i[0]], i[1]])
            else:
                stack.pop()
    if not stack and not incorrects:
        return incorrects
    elif stack:
        for i in stack:
            incorrects.append([rmapping[i[0]], i[1]])
    queue.put(sorted(incorrects, key=lambda x: x[1]))


# Test run
# print(get_unmatched("{\n()\n([)\n[]\n}\n{"))


def combine_expressions(exp_list):
    return [x for x in exp_list]


queue = mp.Queue()


def combine_to_list(characters_list):
    temp = []
    for i in characters_list:
        for j in i:
            if j:
                temp.append(j)
    return temp


def p_check(expression):
    # Replace 4 with some calculated variable based on the size.
    expression_list = split_expression(expression, 4)
    processes = []
    for i, exp in enumerate(expression_list):
        processes.append(mp.Process(target=get_unmatched, args=(exp,)))
    for p in processes:
        p.start()
    for p in processes:
        p.join()
    results = [queue.get() for _ in processes]
    print(results)
    combined_exps = combine_to_list(results)
    print(is_matched(combined_exps))


# Temp call
# p_check("{()\n()()\n[]\n[()]\n[()]\n()[()()\n[()]\n]}")
p_check("{()()[()}{()()}")


def run(jsfile):
    s = ""
    with open(jsfile) as fp:
        line = fp.readline()
        s += line
        while line:
            line = fp.readline()
            s += line
    return is_matched(jsfile, s)
