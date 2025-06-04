import sys
import math
from functools import partial
from operator import itemgetter

input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

T = int(input())
query = [tuple(map(int, input().split())) for _ in range(T)]

def solve_quadratic(a, b, c):
    disc = math.fsum([b * b, -4 * a * c])
    return (-b + math.sqrt(disc)) / (2 * a)

def concentric_partition(r, R, d):
    # Use cross-ratio invariance under inversion
    ratio = ((d + r + R) * (d - R - r)) / (4 * r * R)
    R_sol = solve_quadratic(1, -2 - 4 * ratio, 1)
    r_eff = (R_sol - 1) / 2
    theta = math.asin(r_eff / (1 + r_eff))
    return int(math.pi // theta)

answer = map(
    lambda data: str(
        concentric_partition(
            data[2], data[5], math.hypot(data[3] - data[0], data[4] - data[1])
        )
    ),
    query,
)

print(*answer, sep='\n')