from functools import reduce
a, b, c = map(int, input().split())
k = int(input())
nums = [a, b, c]
max_idx = max(range(3), key=nums.__getitem__)
nums[max_idx] <<= k
print(sum(nums))