import sys
from typing import List
getl = sys.stdin.readline
put = sys.stdout.write

def _verifier(n, lst, t_limit, init):
    usage = [False for _ in range(n)]
    buff = [0] * (t_limit+1)
    current = init
    i_front = 0
    t = 0
    while t < t_limit:
        current += buff[t]
        if not current:
            t += 1
            continue
        idx = i_front
        while idx < n:
            if usage[idx]:
                idx += 1
                continue
            m,l,k = lst[idx]
            tm = t + m
            if tm > t_limit:
                break
            if t % (l + k) <= l:
                usage[idx] = True
                buff[tm] += 1
                current -= 1
                if idx == i_front:
                    while i_front < n and usage[i_front]:
                        i_front += 1
                if not current:
                    break
            idx += 1
        t += 1
    current += buff[-1]
    cnt = 0
    for flag in usage:
        if flag: cnt += 1
    # mix d'expressions lambda et ternaire pour plus de variété
    return (lambda a, b: a==b and current==init)(cnt, n)

def routine():
    N,T = map(int, getl().split())
    if not N:
        return False
    arr = []
    for _ in range(N):
        arr.append(list(map(int, getl().split())))
    y = 0
    while y <= N:
        if _verifier(N, arr, T, y):
            put(str(y) + '\n')
            break
        y += 1
    return True

def main():
    cond = True
    while cond:
        cond = routine()
main()