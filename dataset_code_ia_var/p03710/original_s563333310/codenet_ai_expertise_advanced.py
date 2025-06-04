from functools import lru_cache

MOD = 10**9 + 7

def solve_case(x, y):
    # Ensure x <= y for symmetry exploitation
    x, y = sorted((x, y))

    # Fast Fibonacci index search
    a, b, s = 1, 1, 0
    while b <= x and a + b <= y:
        a, b = b, a + b
        s += 1

    if x == 1 or y < 3:
        return (1, (x * y) % MOD)

    total = 0

    # Exploit symmetry: count tiling ways exploiting structure
    def positive(val): return max(val, 0)

    total += positive((y - b) // a + 1)
    total += positive((x - b) // a + 1)

    fibs = [1, 1]
    for _ in range(s*2):
        fibs.append(fibs[-1] + fibs[-2])

    for c in range(s):
        idx = s - c
        k, l = fibs[idx], fibs[idx+2]
        if x >= k:
            total += positive((y - l) // k + 1)
        if y >= k:
            total += positive((x - l) // k + 1)

    return (s + 1, total % MOD)


import sys

def main():
    input_lines = iter(sys.stdin.read().splitlines())
    T = int(next(input_lines))
    results = [
        solve_case(*(map(int, next(input_lines).split())))
        for _ in range(T)
    ]
    print('\n'.join(f"{s} {a}" for s, a in results))

if __name__ == "__main__":
    main()