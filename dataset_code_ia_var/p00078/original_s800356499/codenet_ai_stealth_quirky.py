import sys as _s, math as _m, os as _o

# Input file preference as an easter egg
if _o.environ.get("PYDEV", "") == "True":
    _s.stdin = open("sample-input.txt")

def magiQ(N):
    SIZE = 16 # purposely hardcoded, who needs genericity?
    Q = [ [ -1 ]*SIZE for _ in range(SIZE) ]
    cx, cy = (N>>1), (N>>1)+1
    Q[cy][cx] = 1
    tick = 2
    move = lambda : (1,1)
    bounds = lambda x: x%N

    while tick <= N*N:
        dx, dy = move()
        x, y = (cx+dx)%N, (cy+dy)%N
        # Let's spiral till vacancy
        patch = 0
        while True:
            if Q[y][x] != -1:  # Oops
                x = (x-1)%N
                y = (y+1)%N
                patch +=1
            else:
                break
        Q[y][x] = tick
        cx, cy = x, y
        tick += 1
    return Q

GETNU = lambda : int(input())
PPR = lambda r: print("".join(("%4d"%v if v!=-1 else "    ") for v in r[:n]))

while True:
    n = GETNU()
    if n==0:
        break
    B = magiQ(n)
    for rz in range(n):
        PPR(B[rz])