from collections import defaultdict, deque
from heapq import heappush, heappop
import sys
import math
import bisect
import random

def LI():
    return [int(x) for x in sys.stdin.readline().split()]

def I():
    return int(sys.stdin.readline())

def LS():
    return [list(x) for x in sys.stdin.readline().split()]

def S():
    res = list(sys.stdin.readline())
    if res[-1] == "\n":
        return res[:-1]
    return res

def IR(n):
    return [I() for i in range(n)]

def LIR(n):
    return [LI() for i in range(n)]

def SR(n):
    return [S() for i in range(n)]

def LSR(n):
    return [LS() for i in range(n)]

sys.setrecursionlimit(1000000)
mod = 1000000007

def dot_product(a, b):
    return sum([a[i]*b[i] for i in range(len(a))])

def to_float(x):
    return float(x)

def to_radian(deg):
    return deg*math.pi/180

def from_radian(rad):
    return rad*180/math.pi

def compute_new_vector(s, t, x, y):
    return [s - x, t - y]

def init_vector():
    return [1, 0]

def vector_square_sum(v):
    return dot_product(v, v)

def cosine_angle(v, nv):
    denominator = (vector_square_sum(v) * vector_square_sum(nv))**0.5
    if denominator == 0:
        return 1.0
    return dot_product(v, nv) / denominator

def angle_between_vectors(v, nv):
    cos_angle = cosine_angle(v, nv)
    # clamp cos_angle to valid range in case of floating point errors
    cos_angle = max(-1.0, min(1.0, cos_angle))
    return math.acos(cos_angle)

def update_ans(ans, m):
    return min(ans, m)

def permutations_of_range(n):
    from itertools import permutations
    return permutations(range(n), n)

def read_input():
    n = I()
    p = LIR(n)
    return n, p

def process_permutation(l, p):
    x, y = 0, 0
    m = 0
    v = init_vector()
    for i in l:
        s, t = p[i]
        nv = compute_new_vector(s, t, x, y)
        m += angle_between_vectors(v, nv)
        x, y = s, t
        v = [nv[0], nv[1]]
    s, t = 0, 0
    nv = compute_new_vector(s, t, x, y)
    m += angle_between_vectors(v, nv)
    return m

def find_minimal_angle(n, p):
    ans = float("inf")
    for l in permutations_of_range(n):
        m = process_permutation(l, p)
        ans = update_ans(ans, m)
    return ans

def print_result(ans):
    res = from_radian(ans)
    print(res)

def solve():
    n, p = read_input()
    min_angle = find_minimal_angle(n, p)
    print_result(min_angle)

if __name__ == "__main__":
    solve()