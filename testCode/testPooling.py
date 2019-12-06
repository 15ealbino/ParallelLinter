from multiprocessing import Pool


def cube(x):
    return x ** 3


pool = Pool(processes=4)
results = [pool.apply_async(cube, args=(x,)) for x in range(1, 7)]
output = [p.get() for p in results]
print(output)
