import math

n = input()
for i in range(n):
    xa, ya, ra, xb, yb, rb = map(float, raw_input().split())
    r = ((xa-xb)**2 + (ya-yb)**2)**.5
    if ra+rb<r: print 0
    elif abs(ra-rb)<=r: print 1
    elif ra-rb>r: print 2
    else: print -2