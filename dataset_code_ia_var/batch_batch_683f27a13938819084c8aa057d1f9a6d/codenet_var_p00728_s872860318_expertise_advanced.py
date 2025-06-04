from itertools import islice
from statistics import mean

while (n := int(input())) != 0:
    nums = [int(input()) for _ in range(n)]
    mi, ma = min(nums), max(nums)
    result = int(mean(x for x in nums if x not in (mi, ma) or nums.count(x) > 1))
    print(result)