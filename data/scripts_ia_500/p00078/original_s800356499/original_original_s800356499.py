# Aizu Problem 0078: Magic Square
#
import sys, math, os

# read input:
PYDEV = os.environ.get('PYDEV')
if PYDEV=="True":
    sys.stdin = open("sample-input.txt", "rt")

def magic_square(n):
    sq = [[0 for _ in range(16)] for __ in range(16)]
    nowx, nowy = n // 2, n // 2 + 1
    sq[nowy][nowx] = 1
    for i in range(2, n**2 + 1):
        nowx += 1
        nowy += 1
        while True:
            if nowx >= n:
                nowx = 0
            if nowx < 0:
                nowx = n - 1
            if nowy >= n:
                nowy = 0
            if sq[nowy][nowx] != 0:
                nowx -= 1
                nowy += 1
            if sq[nowy][nowx] == 0 and 0 <= nowx and nowx < n and 0 <= nowy and nowy < n:
                break
        sq[nowy][nowx] = i
    return sq[:n]

while True:
    n = int(input())
    if n == 0:
        break
    sq = magic_square(n)
    for row in sq:
        out = ""
        for k in row[:n]:
            ks = str(k)
            ks = ' ' * (4 - len(ks)) + ks
            out += ks
        print(out)