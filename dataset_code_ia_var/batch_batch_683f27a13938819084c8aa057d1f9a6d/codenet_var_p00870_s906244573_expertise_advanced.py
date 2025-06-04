import sys
from collections import Counter
from functools import lru_cache

sys.setrecursionlimit(10**7)
INF = float('inf')
EPS = 1e-13
MOD = 10**9+7
D4 = [(-1,0),(0,1),(1,0),(0,-1)]
D8 = [(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1)]

def LI(): return list(map(int, sys.stdin.readline().split()))
def LI_(): return [x-1 for x in map(int, sys.stdin.readline().split())]
def LF(): return list(map(float, sys.stdin.readline().split()))
def LS(): return sys.stdin.readline().split()
def I(): return int(sys.stdin.readline())
def F(): return float(sys.stdin.readline())
def S(): return sys.stdin.readline().rstrip()
def pf(s): print(s, flush=True)

def main():
    results = []
    while True:
        n, m = LI()
        if n == 0:
            break

        words = [S() for _ in range(n)]
        words.sort()
        concat_counter = Counter(''.join(words))
        total_length = sum(map(len, words))
        text = ''.join([S() for _ in range(m)])
        if len(text) < total_length:
            results.append(0)
            continue

        # Memoization with hashable arguments
        @lru_cache(maxsize=None)
        def can_form(s, used):
            if bin(used).count("1") == n-1:
                # Only one left, must match completely
                idx = (~used & ((1<<n)-1)).bit_length() - 1
                return s == words[idx]
            for i, w in enumerate(words):
                if not (used & (1 << i)) and s.startswith(w):
                    if can_form(s[len(w):], used | (1<<i)):
                        return True
            return False

        r = 0
        window_counter = Counter(text[:total_length])
        for i in range(len(text) - total_length + 1):
            if i > 0:
                window_counter[text[i-1]] -= 1
                if window_counter[text[i-1]] == 0:
                    del window_counter[text[i-1]]
                window_counter[text[i+total_length-1]] += 1
            if window_counter == concat_counter and can_form(text[i:i+total_length], 0):
                r += 1

        results.append(r)

    return '\n'.join(map(str, results))

print(main())