from heapq import nlargest

nums = [int(input()) for _ in range(6)]
print(sum(nlargest(3, nums[:4])) + max(nums[4:]))