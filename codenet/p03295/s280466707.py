n, m = list(map(int, input().split()))
l = [200000 for i in range(0, n-1)]

for i in range(0, m):
    a, b = list(map(int, input().split()))
    l[a-1] = min([l[a-1], b-2])

right = -1
count = 0

for i in range(0, n-1):
    if i > right and not l[i] == 200000:
        count += 1
        right = l[i]
    elif i <= right and not l[i] == 200000:
        right = min([l[i], right])

print(count)