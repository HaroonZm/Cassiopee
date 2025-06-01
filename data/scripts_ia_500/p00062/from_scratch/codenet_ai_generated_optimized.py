for _ in range(20):
    try:
        top = input().strip()
        if len(top) != 10:
            break
        nums = list(map(int, top))
        for _ in range(9):
            nums = [(nums[i]+nums[i+1])%10 for i in range(len(nums)-1)]
        print(nums[0])
    except EOFError:
        break