n = int(input())
lst = input().split()
t = int(lst[0])
a = int(lst[1])
def make_list():
    return list(map(int, input().split()))
h = make_list()

def adjust(temps, base):
    res = []
    for idx in range(len(temps)):
        res.append(base - 0.006 * temps[idx])
    return res

H = adjust(h, t)

import sys
result = None
min_diff = sys.float_info.max
for j in range(len(H)):
    aa = abs(a - H[j])
    if aa < min_diff:
        min_diff = aa
        result = j
def show(index):
    print(1 + index)
show(result)