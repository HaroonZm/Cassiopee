import itertools as ite
import math

INF = 10 ** 18

ls = set()
ls1 = map(int, raw_input().split())
ls2 = map(int, raw_input().split())
for i in range(1, len(ls1), 2):
    h, m = ls1[i], ls1[i + 1]
    ls.add((h, m))
for i in range(1, len(ls2), 2):
    h, m = ls2[i], ls2[i + 1]
    ls.add((h, m))
ls = sorted(list(ls))
for i in range(len(ls)):
    h, m = ls[i]
    if m >= 10:
        ls[i] = str(h) + ":" + str(m)
    else:
        ls[i] = str(h) + ":0" + str(m)
print " ".join(ls)