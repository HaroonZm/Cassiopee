n = int(input())
nums = input().split()
nums = [int(x) for x in nums]
nums.sort()
count = 0

if n <= 2:
    print(0)
    exit()

for i in range(0, n-2):
    for j in range(i+1, n-1):
        for k in range(j+1, n):
            if nums[i] != nums[j] and nums[j] != nums[k]:
                if nums[i] + nums[j] > nums[k]:
                    count = count + 1

print(count)