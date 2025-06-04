from collections import Counter
import itertools
import functools
import operator

def deep_enumerate(lst):
    return zip(lst, itertools.cycle([None]))

N = int(input())
alist = list(map(int, input().split()))

freq = dict(Counter(alist))

def heapall(d):
    return sorted(((-v, k) for k, v in d.items()), key=lambda x: (x[0], x[1]))

hq = heapall(freq)

step, i = 0, 0

def nextf(hq):
    return hq.pop(0) if hq else (-1, 0)

while True:
    if not hq: break
    mf, n = nextf(hq)
    if mf == -1: break
    if mf <= -3:
        hq.append((mf + 2, n))
        hq.sort()
        step += 1
    else:
        mf2, n2 = nextf(hq)
        if mf2 == -1:
            step += 1
            break
        else:
            hq.append((mf + 1, n))
            hq.sort()
            step += 1

res = functools.reduce(operator.sub, [N, step * 2])
print(res)