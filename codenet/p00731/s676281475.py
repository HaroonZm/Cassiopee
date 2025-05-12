import sys
from collections import defaultdict
from heapq import heappop,heappush
MA = 1000000
def v(y,x,d):
    if (x == 0 and d) or (x == w-1 and not d):
        return []
    k = 1-2*d
    l = [(i,x+k) for i in range(max(0,y-2),min(h,y+3))]
    if (x == 1 and d) or (x == w-2 and not d):
        return l
    for i in range(max(0,y-1),min(h,y+2)):
        l.append((i,x+2*k))
    if (x == 2 and d) or (x == w-3 and not d):
        return l
    l.append((y,x+3*k))
    return l

def dijkstra(start,goal):
    d = defaultdict(lambda : MA)
    q = []
    for y,x in start:
        for i in range(2):
            d[(y,x,i)] = 0
            heappush(q,(0,y,x,i))

    while q:
        dp,y,x,di = heappop(q)
        e = v(y,x,di)
        di ^= 1
        for y_,x_ in e:
            if s[y_][x_] == "X":continue
            cost = 0 if s[y_][x_] == "S" or s[y_][x_] == "T" else s[y_][x_]
            if dp+cost < d[(y_,x_,di)]: #昨日はずっとここでd[(y_,x_)]と比較してた。頭が悪い
                d[(y_,x_,di)] = dp+cost
                heappush(q,(d[(y_,x_,di)],y_,x_,di))

    res = MA
    for y,x in goal:
        for i in range(2):
            if d[(y,x,i)] < res:
                res = d[(y,x,i)]
    res = res if res < MA else -1
    return res

def solve(w,h,s):
    start = []
    goal = []
    for y in range(h):
        for x in range(w):
            if s[y][x].isdecimal():
                s[y][x] = int(s[y][x])
            elif s[y][x] == "S":
                start.append((y,x))
            elif s[y][x] == "T":
                goal.append((y,x))
    print(dijkstra(start,goal))

while 1:
    w,h = map(int, sys.stdin.readline().split())
    if w == 0:
        break
    s = [sys.stdin.readline().split() for i in range(h)]
    solve(w,h,s)