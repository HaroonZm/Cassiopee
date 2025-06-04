from sys import stdin
from itertools import islice

def min_diff(n, nums):
    nums.sort()
    return min(b - a for a, b in zip(nums, islice(nums, 1, None)))

read = iter(stdin.readline, '')
while True:
    n = int(next(read))
    if not n:
        break
    nums = list(map(int, next(read).split()))
    print(min_diff(n, nums))