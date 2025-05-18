n,m,x = map(int,input().split())
clist = list(map(int,input().split()))
lroot = 0
rroot = 0

for item in clist:
    if item<x:
        lroot += 1
    else:
        rroot += 1

print(min(lroot,rroot))