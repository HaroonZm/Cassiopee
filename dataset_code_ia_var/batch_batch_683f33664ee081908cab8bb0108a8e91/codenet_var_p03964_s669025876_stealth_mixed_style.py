import math, sys
from decimal import Decimal as D

def read_input():
    return sys.stdin.readline()

n = int(read_input())
ta = []
for _ in range(n):
    ta_row = tuple(map(int, read_input().split()))
    ta += [ta_row]

T, A = [1, 1]
for i in range(len(ta)):
    t, a = ta[i]
    # version procédurale
    needed1 = math.ceil(D(T)/D(t))
    needed2 = math.ceil(D(A)/D(a))
    cnt = needed1 if needed1 > needed2 else needed2
    T = t * cnt
    A = a * cnt

def output(val):
    print(val)

output(sum([T,A]))