import multiprocessing as mp
import time

lst = [x for x in range(1000000)]

output = mp.Queue()
processes = []


def p_add(begin, end, d_set):
    if end - begin < len(d_set) - 1:
        output.put(sum(d_set[begin:end]))
    else:
        mid = int(len(d_set) / 2)
        processes.append(mp.Process(target=p_add, args=(begin, mid, d_set)))
        processes.append(mp.Process(target=p_add, args=(mid, end, d_set)),)


def s_add(lst):
    temp = 0
    for i in lst:
        temp += i
    return temp


pt_s = time.perf_counter()
p_add(0, len(lst), lst)
for p in processes:
    p.start()
for p in processes:
    p.join()
results = [output.get() for p in processes]
pt_e = time.perf_counter()
print(results)
print(f"time: {round(pt_e - pt_s, 7)}")

st_s = time.perf_counter()
res = s_add(lst)
st_e = time.perf_counter()
print(res)
print(f"s time: {round(st_e - st_s, 7)}")
