import sys

def solve():
    readline = sys.stdin.buffer.readline
    mod = 10 ** 9 + 7
    n, a, b = list(map(int, readline().split()))
    print(min(a, b), max(a + b - n, 0))

if __name__ == '__main__':
    solve()