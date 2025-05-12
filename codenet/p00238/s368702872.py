import sys,os
while 1:
    t = int(input())
    if t == 0: break
    n = int(input())
    sf = [list(map(int, input().split())) for _ in range(n)]
    
    time = 0
    for i in sf:
        start,end = i
        if start > end:
            time += end - (start-24)
        else:
            time += end - start
    if time >= t:
        print("OK")
    else:
        print(t-time)