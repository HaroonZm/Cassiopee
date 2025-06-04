from collections import Counter
from itertools import islice

def main():
    n = int(input())
    A = list(map(int, input().split()))
    n2 = int(input())

    # Pré-traitement par index
    index_map = {}
    for idx, val in enumerate(A):
        index_map.setdefault(val, []).append(idx)

    for _ in range(n2):
        b, e, k = map(int, input().split())
        # Binary search pour compter les occurrences en O(log n) si besoin
        from bisect import bisect_left, bisect_right
        idxs = index_map.get(k, [])
        left = bisect_left(idxs, b)
        right = bisect_left(idxs, e)
        print(right - left)

if __name__ == '__main__':
    main()