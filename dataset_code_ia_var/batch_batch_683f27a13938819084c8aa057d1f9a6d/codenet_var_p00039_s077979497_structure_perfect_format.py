import sys

r = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

for e in sys.stdin:
    n = [r[c] for c in e.strip()]
    print(
        sum(
            n[i] * [1, -1][i + 1 < len(n) and n[i] < n[i + 1]]
            for i in range(len(n))
        )
    )