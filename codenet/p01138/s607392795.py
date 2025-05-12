#! /usr/bin/python

import re
import heapq

while 1:
    n = int(raw_input())
    if n==0:break
    q = []
    lg = []
    Max = 0
    for i in range(n):
        t = map(int, re.split(r'\s|:', raw_input()))
        lg.append([t[0]*60*60+t[1]*60+t[2], t[3]*60*60+t[4]*60+t[5]])
    lg.sort()
    for i in range(n):
        while len(q) > 0:
            top = heapq.heappop(q)
            if top > lg[i][0]:
                heapq.heappush(q, top)
                break
        heapq.heappush(q, lg[i][1])
        if Max < len(q):
            Max = len(q)
    print Max