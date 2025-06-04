from sys import stdin

def fun(n, k):
    from itertools import islice, accumulate
    A = [int(next(stdin)) for _ in range(n)]
    if k == 0 or n < k:
        print(0)
        return
    # Precompute sliding window sums in one pass
    window_sum = sum(A[:k])
    max_sum = window_sum
    for i in range(k, n):
        window_sum += A[i] - A[i - k]
        max_sum = max(max_sum, window_sum)
    print(max_sum)

for _ in range(5):
    try:
        n, k = map(int, next(stdin).split())
    except StopIteration:
        break
    if n == 0 and k == 0:
        break
    fun(n, k)