from itertools import permutations

N = int(input())
a = list(map(int, input().split()))
w = list(map(int, input().split()))

min_frustration = float('inf')
for order in permutations(range(N)):
    # Fix first sage to reduce rotations checking equivalent circular permutations
    if order[0] != 0:
        continue
    total = 0
    for i in range(N):
        curr = order[i]
        left = order[i - 1]
        right = order[(i + 1) % N]
        if a[curr] == 0:
            # right-handed: frustrated if left-handed on right
            if a[right] == 1:
                total += w[curr]
        else:
            # left-handed: frustrated if right-handed on left
            if a[left] == 0:
                total += w[curr]
        if total >= min_frustration:
            break
    else:
        if total < min_frustration:
            min_frustration = total

print(min_frustration)