from collections import defaultdict, deque
import sys, heapq, bisect, math, itertools, string, queue, copy, time
sys.setrecursionlimit(10**8)
INF = float('inf')
mod = 10**9 + 7
eps = 10**-7

def inp():
    return int(input())

def inpl():
    return list(map(int, input().split()))

def inpl_str():
    return list(input().split())

while True:
    tmp = input().split()
    H = int(tmp[0]); W = int(tmp[1]); C = int(tmp[2])
    if H == 0:
        break
    pp = []
    for _ in range(H):
        pp.append(list(map(int, input().split())))
    ans = 0

    pr = list(itertools.product(range(1, 7), repeat=4))
    idx = 0
    while idx < len(pr):
        arg = pr[idx]
        colors = list(arg) + [C]
        tmpp = []
        j = 0
        while j < H:
            tmpp.append(pp[j][:])
            j += 1
        i = 0
        while i < len(colors):
            c = colors[i]
            if tmpp[0][0] == c:
                i += 1
                continue
            stack = [(0, 0)]
            s = tmpp[0][0]
            while stack:
                X, Y = stack.pop()
                if not (0 <= X < W and 0 <= Y < H):
                    continue
                if tmpp[Y][X] != s:
                    continue
                tmpp[Y][X] = c
                stack.append((X+1, Y))
                stack.append((X-1, Y))
                stack.append((X, Y+1))
                stack.append((X, Y-1))
            i += 1

        stk = [(0, 0)]
        cnt = 0
        if tmpp[0][0] == C:
            tmpp[0][0] = -1
            stk2 = [(0, 0)]
            while stk2:
                xx, yy = stk2.pop()
                cnt += 1
                for dx, dy in ((1,0),( -1,0), (0,1), (0, -1)):
                    nx, ny = xx + dx, yy + dy
                    if 0 <= nx < W and 0 <= ny < H and tmpp[ny][nx] == C:
                        tmpp[ny][nx] = -1
                        stk2.append((nx, ny))
        ans = max(cnt, ans)
        idx += 1

    print(ans)