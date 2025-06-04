for _ in range(20):
    try:
        line = input()
        if not line:
            break
    except EOFError:
        break
    nums = list(map(int, line.strip()))
    while len(nums) > 1:
        nums = [(nums[i] + nums[i+1]) % 10 for i in range(len(nums)-1)]
    print(nums[0])