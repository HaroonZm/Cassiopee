from math import pow
from operator import sub
from sys import stdin

n = int(stdin.readline())
x = list(map(int, stdin.readline().split()))
y = list(map(int, stdin.readline().split()))

elem_dis = list(map(lambda a, b: abs(sub(a, b)), x, y))

for p in range(1, 4):
    print(pow(sum(pow(d, p) for d in elem_dis), 1/p))

print(max(elem_dis))