N = int(input())
minimum = None
for _ in range(N):
    nums = input().split()
    total = 0
    i = 0
    while i < len(nums):
        total += int(nums[i])
        i += 1
    if minimum is None or total < minimum:
        minimum = total
else:
    print(minimum)