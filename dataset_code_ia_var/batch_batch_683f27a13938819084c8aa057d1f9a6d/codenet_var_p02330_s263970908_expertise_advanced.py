import sys
import bisect
from itertools import product
from operator import itemgetter

def split_subsets(arr):
    n = len(arr)
    yield from ((binmask.count(1), sum(x for b, x in zip(binmask, arr) if b))
                for binmask in product((0, 1), repeat=n))

def main():
    n, K, L, R = map(int, sys.stdin.readline().split())
    a = tuple(map(int, sys.stdin.readline().split()))
    m = (n - 1) // 2
    left, right = a[:m], a[m:]

    # Générer les sous-ensembles pour chaque moitié avec groupement et tri
    from collections import defaultdict
    ls = defaultdict(list)
    for cnt, val in split_subsets(left):
        ls[cnt].append(val)
    for vals in ls.values():
        vals.sort()

    ans = 0
    lenr = len(right)
    for cnt_r, val_r in split_subsets(right):
        cnt_l = K - cnt_r
        if 0 <= cnt_l <= m and K - m <= cnt_r <= K:
            lvals = ls[cnt_l]
            low = L - val_r
            high = R - val_r
            ans += bisect.bisect_right(lvals, high) - bisect.bisect_left(lvals, low)
    print(ans)

if __name__ == '__main__':
    main()