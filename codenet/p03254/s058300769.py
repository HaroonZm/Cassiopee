import sys

ns = lambda: sys.stdin.readline().rstrip()
ni = lambda: int(ns())
na = lambda: [int(x) for x in ns().split()]
nall = lambda: [int(x) for x in sys.stdin.readlines()]

def main():
    n, x = na()
    aa = na()

    aa.sort()
    #print(aa)

    c = 0
    for a in aa:
        x -= a
        if x >= 0:
            c += 1
            
    if x > 0:
        c -= 1
    print(c)

main()