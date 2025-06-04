a, b, c, d, e = input().split()
a = int(a)
b = int(b)
c = int(c)
d = int(d)
e = int(e)

nums = [a, b, c, d, e]

# tri simple avec bubble sort pour un débutant
for i in range(len(nums)):
    for j in range(len(nums)-1):
        if nums[j] < nums[j+1]:
            temp = nums[j]
            nums[j] = nums[j+1]
            nums[j+1] = temp

for num in nums:
    print(num, end=' ')