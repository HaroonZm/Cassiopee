def min_rotations(k, initial, target):
    diffs = []
    for i in range(k):
        a, b = int(initial[i]), int(target[i])
        d = (b - a) % 10
        diffs.append(d)
    rotations = 0
    i = 0
    while i < k:
        if diffs[i] == 0:
            i += 1
            continue
        d = diffs[i]
        j = i
        while j < k and diffs[j] == d:
            j += 1
        rotations += 1
        for x in range(i, j):
            diffs[x] = 0
        i = j
    return rotations

while True:
    k = int(input())
    if k == 0:
        break
    initial, target = input().split()
    print(min_rotations(k, initial, target))