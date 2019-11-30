import multiprocessing as mp
import time
import random
import string

random.seed(123)

output = mp.Queue()


def rand_string(length, pos, output):
    rand_str = "".join(
        random.choice(string.ascii_lowercase + string.ascii_uppercase + string.digits)
        for i in range(length)
    )
    output.put((pos, rand_str))


processes = [mp.Process(target=rand_string, args=(5, x, output)) for x in range(4)]
for p in processes:
    p.start()

for p in processes:
    p.join()

results = [output.get() for p in processes]

print(results)
