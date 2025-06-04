from functools import reduce
from operator import lt

*nums, = map(int, input().split())
comparators = [lt] * (len(nums) - 1)
result = all(map(lambda x: x[0](x[1], x[2]), zip(comparators, nums, nums[1:])))
print(("No", "Yes")[result])