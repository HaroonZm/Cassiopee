from math import comb

def s():
    n, m, r = map(int, input().split())
    r -= n * m
    print(comb(n + r - 1, n - 1) if r >= 0 else 0)

if __name__ == '__main__':
    s()