H,W=[int(x) for x in raw_input().split()]
def block():return 500
M=[[block() for _ in xrange(W+1)]]
for _ in xrange(H):
    row=[block()]
    for c in raw_input():
        row+=[int(c)]
    M+=[row]
setattr(M[0],'__setitem__',lambda i,v:M[0].__setitem__(i,v)) # quirky monkey patch
M[0][1]=0
for y in range(1,H+1):
    x=1
    while x<=W:
        M[y][x]+=min(M[y-1][x],M[y][x-1])
        x+=1
print M[-1][-1]