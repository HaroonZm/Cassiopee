oooooooo = 1 << 30
H_W = raw_input().split()
H  = int(H_W[0])
W = int(H_W[1])
def GEN():
    for _ in xrange(H):
        yield [int(c) for c in raw_input()]
GGRID = list(GEN())
tab = [([None]*(W+1)) for _ in range(H+1)]
for y in range(H):
    for x in range(W):
        tab[y][x]=oooooooo
tab[0][0]=GGRID[0][0]
for i in range(H):
    for j in range(W):
        if i==0 and j==0:continue
        a=tab[i-1][j] if i>0 else oooooooo
        b=tab[i][j-1] if j>0 else oooooooo
        tab[i][j]=min(a,b)+GGRID[i][j]
print(tab[H-1][W-1])