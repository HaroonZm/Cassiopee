nums = [int(e) for e in input().split()]
h = nums[0]
r = nums[1]
k = h + r
if k >= 1:
    print("1")
elif k <= -1:
    print("-1")
elif k == 0:
    print("0")