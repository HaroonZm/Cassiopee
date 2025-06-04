import math
from sys import stdin

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    return a // gcd(a, b) * b

input = stdin.readline
N, M = map(int, input().split())
A = list(map(int, [input().strip() for _ in range(N)]))
B = list(map(int, input().split()))

l = A[0]
for a in A[1:]:
    l = math.gcd(l, a)

r = B[0]
for b in B[1:]:
    r = lcm(r, b)

if l % r != 0:
    print(0)
    exit()

target = l // r
count = 0
i = 1
while i * i <= target:
    if target % i == 0:
        count += 1
        if target // i != i:
            count += 1
    i += 1

print(count)