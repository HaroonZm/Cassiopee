import itertools

nums = [1,2,3,4,5,6,7,8,9]  # possible digits
count = 0

input_list = list(map(int, input().split()))
# Just checking all permutations of digits 1 to 9
for perm in itertools.permutations(nums):
    skip = False
    for i in range(9):
        if input_list[i] != -1 and input_list[i] != perm[i]:
            skip = True
            break  # no need to check further if one doesn't match
    if skip:
        continue

    # This condition seems like some puzzle or magic sum check
    val = perm[0] + perm[2] + perm[5] - perm[8] + (perm[1] + perm[4] - perm[7]) * 10 + (perm[3] - perm[6]) * 100
    if val == 0:
        count += 1

print(count)