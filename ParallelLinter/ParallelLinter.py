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
    temp = [expression[i : i + n] for i in range(0, len(expression), n)]
    return temp


def is_already_matched(expression, exp_index):
    opening = tuple("({[")
    closing = tuple(")}]")
    mapping = dict(zip(opening, closing))
    stack = []
    line_number = 1

    for letter in expression:
        if letter is "\n":
            line_number += 1
        elif letter in opening:
            stack.append((mapping[letter], line_number))
        elif letter in closing:
            if not stack:
                queue.put((False, exp_index))
                return
            elif letter != stack[-1][0]:
                queue.put((False, exp_index))
                return
            else:
                stack.pop()
    if not stack:
        queue.put((True, exp_index))
        return
    else:
        queue.put((False, exp_index))
        return


def combine_expressions(exp_list):
    new_list_amount = len(exp_list) // 2
    new_list = []
    for lst in range(0, len(exp_list), new_list_amount):
        new_list.append(exp_list[lst : lst + 2])
    return new_list


queue = mp.Queue()


def p_check(expression):
    """
    >>> p_check('{()()()[][()][()]()[()()[()]]}')
    [(False, 0), (False, 1), (False, 2), (False, 3)]
    """
    expression_list = split_expression(expression, 4)
    processes = []
    for i, exp in enumerate(expression_list):
        processes.append(mp.Process(target=is_already_matched, args=(exp, i)))
    for p in processes:
        p.start()
    for p in processes:
        p.join()
    results = [queue.get() for _ in processes]
    temp = []
    combined_exps = []
    for res in results:
        if res[0] is False:
            temp.append(res)
        elif res[1] is True:
            temp.append([])
        if len(temp) is 2:
            combined_exps.append(combine_expressions(temp))


# Temp call
p_check("{()()()[][()][()]()[()()[()]]}")


def is_matched(expression):
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


# def is_matched(file_name, expression):
#     opening = tuple("({[")
#     closing = tuple(")}]")
#     mapping = dict(zip(opening, closing))
#     stack = []
#     line_number = 1
#     return_str = ""

#     output = mp.Queue()

#     processes = [
#         mp.Process(target=get_depth, args=(expression, p, i, output))
#         for i, p in enumerate(expression)
#         if p in opening or p in closing
#     ]

#     for p in processes:
#         p.start()

#     for p in processes:
#         p.join()

#     results = [output.get() for p in processes]

#     print(results)

#     # Match equal depth (), {}, [] characters


def run(jsfile):
    s = ""
    with open(jsfile) as fp:
        line = fp.readline()
        s += line
        while line:
            line = fp.readline()
            s += line
    return is_matched(jsfile, s)
