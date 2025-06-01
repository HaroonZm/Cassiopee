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
    for i in range(len(nums)):
        nums[i] = int(nums[i])
    for i in range(len(nums)):
        if i % 2 != 0:
            nums[i] = -nums[i]
    i = 0
    while i <= len(nums):
        try:
            if nums[i] < 0:
                nums[i] += 10
                if i == len(nums) - 1:
                    nums.append(0)
                nums[i + 1] += 1
            elif nums[i] == 10:
                nums[i] = 0
                if i == len(nums) - 1:
                    nums.append(0)
                nums[i + 1] -= 1
            i += 1
        except IndexError:
            break
    if minus:
        del nums[0]
    output = ''
    for digit in reversed(nums):
        output += str(digit)
    print output