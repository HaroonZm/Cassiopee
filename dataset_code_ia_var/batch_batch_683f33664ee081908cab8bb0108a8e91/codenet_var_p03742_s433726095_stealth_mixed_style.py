def eval_diff():
    nums = input().split(' ')
    a = int(nums[0])
    b = int(nums[1])
    check = lambda m, n: "Alice" if abs(m - n) >= 2 else "Brown"
    print(check(a, b))
eval_diff()