n = int(input())
a = list(map(int, input().split()))
sum_a = [0]
i = 0
while i < n:
    sum_a.append(sum_a[-1] + a[i])
    i += 1
sum_a = sum_a[1:-1]
total = 0
for x in a:
    total += x
i = 0
while i < n - 1:
    sum_a[i] = abs(total / 2 - sum_a[i])
    i += 1
min_val = sum_a[0]
i = 1
while i < len(sum_a):
    if sum_a[i] < min_val:
        min_val = sum_a[i]
    i += 1
print(int(min_val * 2))