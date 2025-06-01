while True:
    nums = raw_input()
    nums = nums.strip()
    if nums == '0':
        break

    nums = list(nums)
    nums.reverse()

    minus = False
    if nums[-1] == '-':
        minus = True
        nums.pop()
        nums.insert(0, '0')

    for i in range(len(nums)):
        nums[i] = int(nums[i])

    for i in range(len(nums)):
        if i % 2 == 1:
            nums[i] = -nums[i]

    i = 0
    while i < len(nums):
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

    if minus:
        nums.pop(0)

    nums.reverse()
    result = ''
    for n in nums:
        result += str(n)
    print result