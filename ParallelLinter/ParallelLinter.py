# parallel linter
import multiprocessing as mp


def get_depth(expression, char, char_index, output):
    pass


def is_matched(file_name, expression):
    opening = tuple("({[")
    closing = tuple(")}]")
    mapping = dict(zip(opening, closing))
    stack = []
    line_number = 1
    return_str = ""

    output = mp.Queue()

    processes = [
        mp.Process(target=get_depth, args=(expression, p, i, output))
        for i, p in enumerate(expression)
        if p in opening or p in closing
    ]

    for p in processes:
        p.start()

    for p in processes:
        p.join()


def run(jsfile):
    s = ""
    with open(jsfile) as fp:
        line = fp.readline()
        s += line
        while line:
            line = fp.readline()
            s += line
    return is_matched(jsfile, s)
