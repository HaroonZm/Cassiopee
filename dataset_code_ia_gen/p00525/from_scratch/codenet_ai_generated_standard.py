import sys
input=sys.stdin.readline
W,H,N=map(int,input().split())
vertical=set([0,W])
horizontal=set([0,H])
for _ in range(N):
    A,B,C,D=map(int,input().split())
    if A==C:
        vertical.add(A)
    else:
        horizontal.add(B)
print((len(vertical)-1)*(len(horizontal)-1))