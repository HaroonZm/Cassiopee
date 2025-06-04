import re
import heapq

while 1:
    n = int(raw_input())
    if n == 0:
        break
    q = []
    lg = []
    Max = 0
    i = 0
    while i < n:
        t = map(int, re.split(r'\s|:', raw_input()))
        lg.append([t[0]*3600 + t[1]*60 + t[2], t[3]*3600 + t[4]*60 + t[5]])
        i += 1
    lg.sort()
    i = 0
    while i < n:
        while len(q) > 0:
            top = heapq.heappop(q)
            if top > lg[i][0]:
                heapq.heappush(q, top)
                break
        heapq.heappush(q, lg[i][1])
        if Max < len(q):
            Max = len(q)
        i += 1
    print Max