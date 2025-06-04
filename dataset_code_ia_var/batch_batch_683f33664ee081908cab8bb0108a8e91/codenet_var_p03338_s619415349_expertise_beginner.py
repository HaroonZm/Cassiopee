N = int(input())
S = input()

left = {}
right = {}

for c in S:
    if c in right:
        right[c] += 1
    else:
        right[c] = 1

left_side = {}
max_common = 0

for c in S:
    if c in left_side:
        left_side[c] += 1
    else:
        left_side[c] = 1

    right[c] -= 1
    if right[c] == 0:
        del right[c]

    common = 0
    for key in left_side:
        if key in right:
            common += 1
    if common > max_common:
        max_common = common

print(max_common)