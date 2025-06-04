import sys
import bisect

size_limits = [60, 80, 100, 120, 140, 160]
weight_limits = [2, 5, 10, 15, 20, 25]
prices = [600, 800, 1000, 1200, 1400, 1600]

def get_price(size, weight):
    s_idx = bisect.bisect_left(size_limits, size)
    if s_idx == len(size_limits):
        return 0
    w_idx = bisect.bisect_left(weight_limits, weight)
    if w_idx == len(weight_limits):
        return 0
    idx = max(s_idx, w_idx)
    return prices[idx]

input = sys.stdin.readline
while True:
    n = int(input())
    if n == 0:
        break
    total = 0
    for _ in range(n):
        x,y,h,w = map(int, input().split())
        size = x + y + h
        p = get_price(size, w)
        total += p
    print(total)