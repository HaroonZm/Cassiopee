from heapq import nsmallest
from itertools.islice

nums = [int(input()) for _ in range(6)]
group1, group2 = nums[:4], nums[4:]

sum1 = sum(islice(sorted(group1), 1, None))
sum2 = sum(islice(sorted(group2), 1, None))

print(sum1 + sum2)