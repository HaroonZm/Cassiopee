from sys import stdin

def solve():
    n, m = map(int, stdin.readline().split())
    print(min(m // 2, n + (m - 2 * n) // 4 if n <= m // 2 else 0))

solve()