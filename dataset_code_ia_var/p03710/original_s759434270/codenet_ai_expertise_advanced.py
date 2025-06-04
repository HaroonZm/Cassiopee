from sys import stdin
from itertools import islice

MOD = 10**9 + 7

def advanced_f(a, l, k):
    return max(0, (a - l) // k + 1)

def solve(x, y):
    x, y = sorted((x, y))
    s, i, j, k, l = -1, 1, 1, 1, 1
    while l <= x and k + l <= y:
        k, l = l, k + l
        s += 1
    a = advanced_f(y, l, k) + advanced_f(x, l, k)
    fib_cache = [(1, 1)]
    for _ in range(s):
        prev1, prev2 = fib_cache[-1]
        fib_cache.append((prev2, prev1 + prev2 * 2))
    for c in range(s):
        k, l = fib_cache[s - c]
        for _ in range(s - c):
            k, l = l, k + l
        a += (y >= k) * advanced_f(x, l, k) + (x >= k) * advanced_f(y, l, k)
    if x < 2 or y < 3:
        return 1, x * y % MOD
    else:
        return s + 1, a % MOD

def main():
    input_iter = map(str.strip, islice(stdin, 1, None))
    for _ in range(int(stdin.readline())):
        x, y = map(int, stdin.readline().split())
        s, result = solve(x, y)
        print(s, result)

if __name__ == '__main__':
    main()