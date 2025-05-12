from __future__ import division,print_function
try:
    input = raw_input
except NameError:
    pass

from datetime import datetime
import math

MAXW = 1001

def solve(n, read, write):
    sumR = sum(read)
    sumW = sum(write)

    next = []
    base = -1
    for i in range(n):
        if read[i] < sumR // 2:
            next.append((read[i], write[i]))
        else:
            base = read[i]
    if (len(next) == n):
        print(sumR + sumW)
        return

    dp = [False] * MAXW
    dp[0] = True
    for i in range(n - 1):
        tmp = dp[:]
        for j in range(base + 1):
            if dp[j]:
                na = j + next[i][0]
                nb = j + next[i][0] + next[i][1]
                if na <= base:
                    tmp[na] = True
                if nb <= base:
                    tmp[nb] = True
        dp = tmp
    res = 0
    for i in range(base + 1):
        if dp[i]:
            res = base - i
    print(sumR + sumW + res)

def main():
    while True:
        n = int(input())
        if n == 0: return
        read = []
        write = []
        for i in range(n):
            r, w = map(int, input().split())
            read.append(r)
            write.append(w)
        solve(n, read, write)

main()