from sys import stdin
import bisect

while(True):
    try:
        *ls,v1,v2 = list(map(int,stdin.readline().split(",")))
        rs = [sum(ls[:i+1]) for i in range(len(ls))]
        idx = bisect.bisect_left(rs,rs[-1]*v1/(v1+v2))
        print(idx+1)
    except:
        break