n = input()
for i in range(n):
    nums = raw_input().split()
    x = int(nums[0])
    y = int(nums[1])
    b = int(nums[2])
    p = int(nums[3])
    cost1 = x * b + y * p
    if b > 5:
        b2 = b
    else:
        b2 = 5
    if p > 2:
        p2 = p
    else:
        p2 = 2
    cost2 = (x * b2 + y * p2) * 0.8
    if cost1 < cost2:
        result = int(cost1)
    else:
        result = int(cost2)
    print "%d" % result