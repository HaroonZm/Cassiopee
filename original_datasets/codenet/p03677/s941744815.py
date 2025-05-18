import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

import itertools

N,M,*A = map(int,read().split())

def f(x,y,k):
    if x > y:
        y += M
    if k <= x:
        k += M
    if k <= y:
        return (y-k) + 1
    return y-x

add_X = 0
add_DX = 0
DDX = [0] * M
for x,y in zip(A,A[1:]):
    x -= 1
    y -= 1
    a = f(x,y,M-2)
    b = f(x,y,M-1)
    add_X += b
    add_DX += b-a
    d = y - x
    if d < 0:
        d += M
    DDX[(y+1)%M] += d
    DDX[(y+2)%M] -= (d-1)
    DDX[(x+2)%M] -= 1

DX = [add_DX + y for y in itertools.accumulate(DDX)]
X = [add_X + y for y in itertools.accumulate(DX)]

answer = min(X)
print(answer)