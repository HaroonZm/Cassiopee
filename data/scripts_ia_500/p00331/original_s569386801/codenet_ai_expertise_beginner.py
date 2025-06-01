nums = input().split()
h = int(nums[0])
r = int(nums[1])

k = h + r

if k >= 1:
    print("1")
else:
    if k <= -1:
        print("-1")
    else:
        if k == 0:
            print("0")