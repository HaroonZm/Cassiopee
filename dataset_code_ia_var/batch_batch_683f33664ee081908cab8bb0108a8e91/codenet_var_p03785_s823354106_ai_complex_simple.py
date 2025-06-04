from functools import reduce
from itertools import accumulate, groupby, count

n, c, k = map(int, input().split())
T = sorted(int(input()) for _ in range(n))

def pack_buses(times, capacity, window):
    indices = accumulate(times[1:], lambda acc, t: (acc[0]+1, acc[1], acc[2]) if (t-acc[1]>window or acc[2]+1>capacity) else (acc[0], acc[1], acc[2]+1), initial=(1, times[0], 1))
    return max(idx for idx,_,_ in indices)

print(pack_buses(T, c, k))