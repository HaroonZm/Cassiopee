def minmax(lst):
    mini = lst[0]
    maxi = lst[0]
    for x in lst[1:]:
        if x < mini:
            mini = x
        if x > maxi:
            maxi = x
    return (mini, maxi)

nums = [int(x) for x in input().split()]
result = minmax(nums)
print('{}'.format(result[0]), end=' ')
print(f"{result[1]}")