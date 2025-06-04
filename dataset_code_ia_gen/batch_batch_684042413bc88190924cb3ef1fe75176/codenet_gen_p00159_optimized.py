import sys
input = sys.stdin.readline

while True:
    n = int(input())
    if n == 0:
        break
    best_p = None
    best_diff = float('inf')
    for _ in range(n):
        p, h, w = map(int, input().split())
        bmi = w / ((h / 100) ** 2)
        diff = abs(bmi - 22)
        if diff < best_diff or (diff == best_diff and p < best_p):
            best_diff = diff
            best_p = p
    print(best_p)