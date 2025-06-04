from functools import lru_cache
from sys import stdin

DIV = 100000

def process_cases():
    for line in stdin:
        nms = line.strip()
        if not nms: continue
        n, m, s = map(int, nms.split())
        if n == 0:
            break

        @lru_cache(maxsize=None)
        def dp(i, j):
            if i == 0 and j == 0:
                return 1
            if i < 0 or j < 0:
                return 0
            # Inclusion-Exclusion Principle for optimization
            res = (dp(i-1, j) + dp(i, j-i) - dp(i-1, j-m-1)) % DIV if j-i >= 0 else dp(i-1, j)
            return res

        # Inline DP for memory optimization and maximum efficiency.
        result = 0
        table = [0] * (s+1)
        table[0] = 1
        for i in range(1, n*n + 1):
            cum = [0] * (s+2)
            for j in range(1, s+2):
                cum[j] = (cum[j-1] + table[j-1]) % DIV
            for j in range(s, -1, -1):
                left = cum[j-i+1] if j - i + 1 >= 0 else 0
                right = cum[j-m] if j - m >= 0 else 0
                table[j] = (left - right + DIV) % DIV
        print(table[s])
        
process_cases()