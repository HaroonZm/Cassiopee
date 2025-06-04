from sys import stdin
from itertools import islice

MOD = 10**9 + 7

def solve(x, y):
    x, y = sorted((x, y))
    if x == 1 or y < 3:
        return (1, x * y % MOD)

    # Génère la suite de Fibonacci jusqu'à dépasser x ou y
    fibs = [1, 1]
    while fibs[-1] <= x and fibs[-2] + fibs[-1] <= y:
        fibs.append(fibs[-2] + fibs[-1])

    s = len(fibs) - 2
    a = max(0, (y - fibs[-1]) // fibs[-2] + 1) + max(0, (x - fibs[-1]) // fibs[-2] + 1)

    for idx in range(s):
        k, l = fibs[idx+1], fibs[idx] + 2*fibs[idx+1]
        # Trouver la position de l et k après s-idx applications récurrentes
        for _ in range(s - idx):
            k, l = l, k + l
        if x >= k:
            a += max(0, (y - l) // k + 1)
        if y >= k:
            a += max(0, (x - l) // k + 1)
    return (s + 1, a % MOD)

def main():
    input_lines = map(str.strip, stdin)
    T = int(next(input_lines))
    outputs = []
    for line in islice(input_lines, T):
        x, y = map(int, line.split())
        res = solve(x, y)
        print(*res)

main()