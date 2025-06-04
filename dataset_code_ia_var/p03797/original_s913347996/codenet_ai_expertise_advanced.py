from sys import stdin

def solve():
    n, m = map(int, stdin.readline().split())
    if m > n << 1:
        rem = m - (n << 1)
        print(n + (rem >> 2))
    elif m == n << 1:
        print(n)
    else:
        print(m >> 1)

solve()