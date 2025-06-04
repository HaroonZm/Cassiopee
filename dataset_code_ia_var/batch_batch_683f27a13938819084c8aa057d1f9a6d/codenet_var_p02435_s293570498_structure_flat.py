from collections import deque
import sys
input = sys.stdin.readline

n1, n2 = map(int, input().split())
wl = []
for _ in range(n1):
    wl.append(deque())
for _ in range(n2):
    l = list(map(int, input().split()))
    if l[0] == 0:
        wl[l[1]].append(l[2])
    elif l[0] == 1:
        if len(wl[l[1]]) != 0:
            print(wl[l[1]][-1])
    elif l[0] == 2:
        if len(wl[l[1]]) != 0:
            wl[l[1]].pop()