while True:
    nums = input().split()
    n = int(nums[0])
    m = int(nums[1])
    if n == 0 and m == 0:
        break
    a = input().split()
    for i in range(len(a)):
        a[i] = int(a[i])
    max_val = m // n
    total = 0
    for i in a:
        if i < max_val:
            total = total + i
        else:
            total = total + max_val
    print(total)