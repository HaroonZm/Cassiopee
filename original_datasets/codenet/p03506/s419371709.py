import sys
input = sys.stdin.readline
N,Q = map(int,input().split())
VW = [tuple(map(int,input().split())) for i in range(Q)]

ans = []
if N==1:
    for v,w in VW:
        ans.append(min(v,w))
else:
    for v,w in VW:
        while v != w:
            if v > w: v,w = w,v
            w = (w+N-2)//N
        ans.append(v)
print(*ans, sep='\n')