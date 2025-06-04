from math import inf, isclose
from sys import stdin

def p_distance(X, Y, p):
    if p == inf:
        return max(map(lambda ab: abs(ab[0] - ab[1]), zip(X, Y)))
    return sum(map(lambda ab: abs(ab[0] - ab[1]) ** p, zip(X, Y))) ** (1 / p)

n = int(stdin.readline())
X = list(map(int, stdin.readline().split()))
Y = list(map(int, stdin.readline().split()))

for p in range(1, 4):
    print(f"{p_distance(X, Y, p):.6f}")

print(f"{p_distance(X, Y, inf):.6f}")