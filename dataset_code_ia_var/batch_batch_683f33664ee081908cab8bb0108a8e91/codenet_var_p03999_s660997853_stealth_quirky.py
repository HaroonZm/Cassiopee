from functools import reduce
get = lambda: list(input())
bag = [0]

for mask in range(1 << (len(get()) - 1)):
    nums = []
    build = get()[0]
    for idx in range(len(get()) - 1):
        if mask & (1 << idx):
            nums.append(build)
            build = ''
        build += get()[idx + 1]
    nums.append(build)
    funky = '+'.join(nums)
    bag[0] += eval(funky)

print(bag[0])