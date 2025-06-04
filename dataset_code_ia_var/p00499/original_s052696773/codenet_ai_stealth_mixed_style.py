from math import ceil

get = lambda: int(input())
vals = [get() for _ in range(5)]
l, a, b, c, d = vals

def compute(a, c):
    return a//c if a % c == 0 else a//c + 1

def decide(a, b, c, d):
    if a%c==0 and b%d==0:
        x = a//c
        y = b//d
    elif a%c==0:
        x = a//c
        y = ceil(b/d)
    elif b%d==0:
        x = ceil(a/c)
        y = b//d
    else:
        x = ceil(a/c)
        y = ceil(b/d)
    return sorted([x, y])
    
r = decide(a, b, c, d)
print((lambda L, y: L-y)(l, r[1]))