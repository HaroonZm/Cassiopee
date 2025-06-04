nums = input().split()
W = int(nums[0])
H = int(nums[1])
x = int(nums[2])
y = int(nums[3])
r = int(nums[4])
if (x - r) >= 0 and (x + r) <= W and (y - r) >= 0 and (y + r) <= H:
    print("Yes")
else:
    print("No")