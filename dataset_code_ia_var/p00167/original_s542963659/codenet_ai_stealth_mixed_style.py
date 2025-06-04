def bSort(N):
    l = []
    i = 0
    while i < N:
        l.append(int(input()))
        i += 1
    swaps = 0
    def sw(a, b):
        tmp = l[a]
        l[a] = l[b]
        l[b] = tmp
    for m in range(len(l)):
        for k in reversed(range(m+1, len(l))):
            if l[k] < l[k-1]:
                sw(k, k-1)
                swaps = swaps + 1
    return swaps

go = 1
from sys import stdin
while go:
    n = int(stdin.readline())
    if not n:
        go = 0
        continue
    print(bSort(n))