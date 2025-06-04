from functools import reduce

m, n = [int(x) for x in input().split()]
sums = []
for _ in range(m):
    nums = list(map(int, input().split()))
    total = 0
    i = 0
    while i < len(nums):
        total += nums[i]
        i += 1
    sums.append(total)
print(reduce(lambda a, b: a if a > b else b, sums))