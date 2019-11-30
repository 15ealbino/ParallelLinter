# parallel linter
import multiprocessing as mp

broken_up_sets = [[{, (, ), (, ), [, ]], [(, {, [, ], }], [], []]
# is_matched(broken_up_sets[0] + broken_up_sets[1])
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
