from functools import reduce

def weird_sum(N, T, t):
    s = T
    f = t[0] + T
    i = 0
    while i < N-1:
        s += T
        if f > t[i+1]:
            s -= f - t[i+1]
        f = t[i+1] + T
        i += 1
    return s

x = input().split()
N = int(x[0])
T = int(x[1])
times = [int(z) for z in input().split()]
def alt_main(times, T, N):
    arr = [times[0]]
    idx = 1
    s = T
    f = arr[0] + T
    for i in range(N-1):
        s += T
        if f > times[idx]:
            s -= f - times[idx]
        f = times[idx] + T
        idx += 1
    return s

if N % 2 == 0:
    print(weird_sum(N, T, times))
else:
    print(alt_main(times, T, N))