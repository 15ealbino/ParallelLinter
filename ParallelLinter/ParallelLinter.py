# parallel linter
import multiprocessing as mp
import math


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
                stack.reverse()
                found_pair = False
                for i in range(len(stack) - 1):
                    if stack[i][0][0] == character[0]:
                        found_pair = True
                if found_pair:
                    for i in stack:
                        if i[0] != character[0]:
                            popped.append(stack.pop())
                        else:
                            stack.pop()
                            break
                    stack.reverse()
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
                        incorrects.append([rmapping[i[0]], i[1]])
                else:
                    stack.reverse()
                    stack.pop()
                    if stack:
                        stack.pop()
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


queue = mp.Queue()

#parallizing string in bins means that the line numbers are gonna be reset for each bin,
#we must run this function to fix the line number for each bin
def fix_line_numbers(exp_list, expression):
    line_number = 0
    new_lines = []
    for i in expression:
        for char in i:
            if char is "\n":
                line_number += 1
        new_lines.append(line_number)
    for index, i in enumerate(exp_list):
        if index != 0:
            for j in i:
                j[1] += new_lines[index - 1]
    return exp_list


exp_list = [
    [["{", 1], ["[", 3]],
    [["]", 1], ["(", 2], ["[", 3], ["(", 3]],
    [[")", 1], ["]", 1], ["[", 2]],
    [["]", 3], ["}", 3]],
]
expression = ["{()\n()()\n[", "]\n[()(]\n[(", ")]\n()[()()", "\n[()]\n]}"]
print(fix_line_numbers(exp_list, expression))


def p_check(expression):
    # Replace 4 with some calculated variable based on the size.
    expression_list = split_expression(expression, 4)
    processes = []
    for i, exp in enumerate(expression_list):
        #set up multi processing
        processes.append(mp.Process(target=get_unmatched, args=(exp,)))
    for p in processes:
        p.start()
    for p in processes:
        p.join()
    results = [queue.get() for _ in processes]
    results = fix_line_numbers(results, expression_list)
    combined_exps = [j for i in results for j in i if j]
    return is_matched(combined_exps)


# Temp call
# print(p_check("{()\n()()\n[]\n[()(]\n[()]\n()[()()\n[()]\n]}"))
# print(p_check("{()()[()}{()()}"))

#build a string from the file convert it from line to line to one big string to evaluate.
def run(jsfile):
    s = ""
    print(f"{jsfile}:\n")
    with open(jsfile) as fp:
        line = fp.readline()
        s += line
        while line:
            line = fp.readline()
            s += line
    return p_check(s)
