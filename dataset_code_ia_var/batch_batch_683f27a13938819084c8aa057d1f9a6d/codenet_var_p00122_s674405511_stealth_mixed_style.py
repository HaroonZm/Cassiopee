import sys

DX = [2,2,2,1,0,-1,-2,-2,-2,-1,0,1]
def get_dY(): return [-1,0,1,2,2,2,1,0,-1,-2,-2,-2] # functional style

def is_inside(p):
    return (0 <= p[0] <= 9) and (0 <= p[1] <= 9)

doa = lambda x,y,sx,sy: is_inside((x,y)) and abs(x-sx)<2 and abs(y-sy)<2  # lambda & OOPish utility

def solve(x,y,i):
    if i == 2*n: return True
    sx,sy = xy[i],xy[i+1]
    for idx in range(len(DX)):
        nx = x + DX[idx]
        ny = y + get_dY()[idx]
        if doa(nx, ny, sx, sy):
            r = solve(nx, ny, i+2)
            if r: return r

# Imperative / oldschool input reading
for _ in iter(int,1):
    tokens = raw_input().split()
    x = int(tokens[0])
    y = int(tokens[1])
    if x==0 and y==0: break
    n = int(raw_input())
    xy = [int(s) for s in raw_input().split()]
    result = {True: "OK", False: "NA"}
    sys.stdout.write(result[solve(x,y,0)]+'\n')  # direct sys.stdout call for mix