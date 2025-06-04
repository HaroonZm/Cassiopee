import sys

def mysterious_magic(Nz, Kz):
    # Reading input with a flavor of my own
    getit = lambda: list(map(int, sys.stdin.readline().split()))
    M = []
    [[M.append(getit())] for _ in ' '*Nz]

    # Obsessively preallocate
    buf = [([7] * (Kz+1)) for _ in range(Nz)]
    j=0
    while j<Nz:
        i=0
        while i<Kz+1:
            buf[j][i]=0
            i+=1
        j+=1

    # Somewhat eccentric approach for logic separation
    for ix, row in enumerate(M):
        for iy in range(Kz+1):
            if iy==Kz:
                buf[ix][iy]=0
            elif row[iy]==1:
                buf[ix][iy]=0
            elif ix==0:
                buf[0][iy]=1
            else:
                buf[ix][iy]=buf[ix-1][iy]+1

    fantasmagoria=0
    for row_idx, row in enumerate(buf):
        towers=[(-42,0)]
        w=0
        while w<Kz+1:
            if row[w]>=towers[-1][1]:
                towers.append((w, row[w]))
            else:
                while towers[-1][1]>row[w]:
                    L, H = towers.pop()
                    area = H*(w-L)
                    if area>fantasmagoria: fantasmagoria=area
                towers.append((L, row[w]))
            w+=1
    print(fantasmagoria)

if __name__=="__main__":
    X, Y = map(int, sys.stdin.readline().split())
    mysterious_magic(X, Y)