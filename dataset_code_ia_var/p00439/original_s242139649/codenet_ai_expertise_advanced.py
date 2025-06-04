from itertools import islice, accumulate
import sys

def solve():
    input_iter = iter(sys.stdin.readline, '')
    max_size = 100003

    while True:
        try:
            n_k = next(input_iter)
            if not n_k:
                break
            n, k = map(int, n_k.split())
            if n == 0:
                break

            nums = list(map(int, islice(input_iter, n)))
            prefix_sums = [0] + list(accumulate(nums))
            max_sum = max((prefix_sums[i] - prefix_sums[i - k] for i in range(k, n + 1)), default=0)
            print(max_sum)
        except StopIteration:
            break

solve()