from sys import stdin
for line in stdin:
    n, *rest = map(int, line.split())
    if n == 0:
        break
    A = sorted(map(int, next(stdin).split()))
    from collections import Counter
    counts = Counter(A)
    majority = next((color for color, cnt in counts.items() if cnt > n // 2), None)
    print(majority if majority is not None else "NO COLOR")