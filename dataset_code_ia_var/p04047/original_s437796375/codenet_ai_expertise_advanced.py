from sys import stdin

_, *numbers = stdin.read().split()
nums = sorted(map(int, numbers))
result = sum(nums[::2])
print(result)