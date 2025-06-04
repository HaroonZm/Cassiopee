from operator import itemgetter

def solve():
    a, b = map(int, input().split())
    hi, lo = max(a, b), min(a, b)
    print(hi + max(hi - 1, lo))

solve()