from itertools import permutations

N = int(input())
a = list(map(int, input().split()))
w = list(map(int, input().split()))

min_frustration = float('inf')
for perm in permutations(range(N)):
    total = 0
    for i in range(N):
        current = perm[i]
        left = perm[i-1]
        right = perm[(i+1) % N]
        if a[current] == 0 and a[right] == 1:
            total += w[current]
        elif a[current] == 1 and a[left] == 0:
            total += w[current]
        if total >= min_frustration:
            break
    if total < min_frustration:
        min_frustration = total

print(min_frustration)