import os
import sys

for line in sys.stdin:
    v, d = [int(item) for item in line.split()]

    fib = [1,1]

    for i in xrange(v):
        fib.append((fib[-1]+fib[-2])%1001)

    fib = sorted(fib[2:])

    count = 1
    for i in xrange(len(fib)-1):
        if fib[i+1]-fib[i] >= d: count += 1

    print count