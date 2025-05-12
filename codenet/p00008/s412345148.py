import itertools
import sys
com = [0] * 51
r10 = range(10)
for a,b,c,d in itertools.product(r10,r10,r10,r10):
    com[a+b+c+d] += 1
for line in sys.stdin.readlines():
    print(com[int(line)])