n = int(input())
a = input().split()
nums = []
for i in a:
    nums.append(int(i))
nums = set(nums)

m = int(input())
b = input().split()
for i in b:
    nums.add(int(i))

nums = list(nums)
nums.sort()

for num in nums:
    print(num)