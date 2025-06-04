from collections import Counter
from sys import stdin

def solve():
    N, *rest = map(int, stdin.read().split())
    freq = Counter(rest)
    odd_count = sum(1 for v in freq.values() if v % 2)
    even_count = len(freq) - odd_count
    ans = odd_count + (even_count if even_count % 2 == 0 else even_count - 1)
    print(ans)

solve()