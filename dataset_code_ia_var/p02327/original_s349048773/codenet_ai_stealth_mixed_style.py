import sys
import collections as col
from functools import reduce

input_stream = sys.stdin

h, w = [int(x) for x in input_stream.readline().split()]

mat = []
for ln in input_stream:
    mat.append(list(map(int, ln.split())))

state = [0]*w

def heights(source):
    global state
    temp = []
    idx = 0
    for val in source[-1]:
        temp.append(0 if val == 1 else state[idx]+1)
        idx += 1
    state = temp.copy()
    return temp

def mx_rect(arr):
    vec = heights(arr)
    res = list()
    dq = col.deque([])
    i = 0
    while i < len(vec):
        if not dq:
            dq.append((i, vec[i]))
        elif vec[i] > dq[-1][1]:
            dq.append((i, vec[i]))
        elif vec[i] < dq[-1][1]:
            last = i-1
            aa = (0,0)
            while dq and vec[i] < dq[-1][1]:
                aa = dq.pop()
                res.append((last-aa[0]+1)*aa[1])
            dq.append((aa[0], vec[i]))
        i += 1
    while dq:
        aa = dq.pop()
        res.append((len(vec)-aa[0])*aa[1])
    try:
        return max(res)
    except ValueError:
        return 0

def compute(matrix):
    resultz = []
    for e in range(h):
        outcome = mx_rect(matrix[:e+1])
        resultz.append(outcome)
    return str(max(resultz) if resultz else 0)

print(compute(mat))