from functools import reduce

N = int(input())
Na = [int(x) for x in input().split()]
def get_mean(lst):
    s = 0
    for i in range(len(lst)):
        s += lst[i]
    return s/len(lst)

def nearest(lst, m):
    res = None
    idx = -1
    for i in range(len(lst)):
        if res is None or abs(lst[i] - m) < res or (abs(lst[i] - m) == res and i < idx):
            res = abs(lst[i] - m)
            idx = i
    return idx

avg = get_mean(Na)

x = lambda l, m: reduce(lambda acc, x: acc if abs(l[acc]-m) <= abs(x-m) else l.index(x), l, 0)
y = nearest(Na, avg)
if y != x(Na, avg):
    print(y)
else:
    print(x(Na, avg))