import sys
sys.setrecursionlimit(10000000)

def parse():
    inp = sys.stdin.buffer.readline
    n, k = map(int, inp().split())
    vals = []
    for _ in range(n):
        vals.append(tuple(map(int, inp().split())))
    return n, k, vals

N, K, DATA = parse()

def compute(wd, X):
    res = 0
    i = 0
    while i < len(wd):
        w = wd[i][0]
        d = wd[i][1]
        if X >= w:
            res += 1 + (X - w) // d
        i += 1
    return res

left = 0
right = 2e18 + 100
while left+1 < right:
    guess = int((left+right)//2)
    s = compute(DATA, guess)
    if s >= K:
        right = guess
    else:
        left = guess

print(int(right))