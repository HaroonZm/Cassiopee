import sys
import math
from collections import defaultdict
from heapq import heapify, heappush, heappop

# Optimized recursion limit and constants
sys.setrecursionlimit(1 << 25)
MOD = 10**9 + 7

# Fast input utilities
def I(): return int(sys.stdin.readline())
def II(): return map(int, sys.stdin.readline().split())
def III(): return list(map(int, sys.stdin.readline().split()))
def Lines(N):
    data = [tuple(map(int, sys.stdin.readline().split())) for _ in range(N)]
    return map(list, zip(*data))

# Main logic with advanced Python features
def main():
    N = I()
    a = [0, *III()]
    size = 3 * N + 1

    red = [0] * size
    blue = [0] * size

    # Left (red) heap: min-heap for smallest N elements, O(N log N)
    q1 = a[1:N+1]
    s_red = sum(q1)
    red[N] = s_red
    heapify(q1)
    for k, val in enumerate(a[N+1:2*N+1], start=N+1):
        heappush(q1, val)
        removed = heappop(q1)
        s_red += val - removed
        red[k] = s_red

    # Right (blue) heap: max-heap for largest N elements, O(N log N)
    q2 = a[2*N+1:3*N+1]
    s_blue = sum(q2)
    blue[2*N] = s_blue
    q2 = [(-x, x) for x in q2]
    heapify(q2)
    for k in range(2*N, N, -1):
        val = a[k]
        heappush(q2, (-val, val))
        removed = heappop(q2)[1]
        s_blue += val - removed
        blue[k-1] = s_blue

    # Vectorized max computation using generator expression
    print(max(red[i] - blue[i] for i in range(N, 2*N+1)))

if __name__ == "__main__":
    main()