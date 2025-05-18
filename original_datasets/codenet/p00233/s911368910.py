while True:
    nums = raw_input().strip()
    if nums == '0':
        break

    nums = list(nums)
    nums.reverse()

    minus = False
    if nums[-1] == '-':
        minus = True
        nums.pop()
        nums = [0] + nums

    nums = map(int, nums)

    for i in range(len(nums)):
        if i % 2 != 0:
            nums[i] = -nums[i]

    for i in range(len(nums) + 1):
        try:
            if nums[i] < 0:
                nums[i] += 10
                if i == len(nums) - 1:
                    nums = nums + [0]
                nums[i + 1] += 1
            elif nums[i] == 10:
                nums[i] = 0
                if i == len(nums) - 1:
                    nums = nums + [0]
                nums[i + 1] -= 1
        except IndexError:
            pass

    if minus:
        del nums[0]

    print ''.join(map(str, reversed(nums)))