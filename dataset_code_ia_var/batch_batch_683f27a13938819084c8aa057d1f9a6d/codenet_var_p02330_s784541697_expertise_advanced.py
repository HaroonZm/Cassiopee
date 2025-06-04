import sys
import bisect
from itertools import compress, accumulate, starmap
from operator import add

def popcount(x):
    return bin(x).count("1")

def get_sums(arr):
    m = len(arr)
    return [
        sorted(
            sum(arr[j] for j in range(m) if (i >> j) & 1)
            for i in range(1 << m) if popcount(i) == bits
        )
        for bits in range(m+1)
    ]

def main():
    n, K, L, R = map(int, sys.stdin.readline().split())
    a = tuple(map(int, sys.stdin.readline().split()))
    m = n//2
    left, right = a[:m], a[m:]
    left_sums = get_sums(left)
    ans = 0
    n_right = n - m
    for mask in range(1 << n_right):
        cnt = popcount(mask)
        if K-m <= cnt <= K:
            val = sum(right[j] for j in range(n_right) if (mask >> j) & 1)
            candidates = left_sums[K-cnt]
            lo = bisect.bisect_right(candidates, R - val)
            hi = bisect.bisect_right(candidates, L - val - 1)
            ans += lo - hi
    print(ans)

if __name__ == '__main__':
    main()