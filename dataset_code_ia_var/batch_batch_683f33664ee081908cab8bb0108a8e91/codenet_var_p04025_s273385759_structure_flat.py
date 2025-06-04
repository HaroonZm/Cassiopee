N = int(input())
a = [int(x) for x in input().split()]
min_a = min(a)
max_a = max(a)
ans = 10**10
i = min_a
while i <= max_a:
    sum_c = 0
    j = 0
    while j < N:
        sum_c += (a[j] - i) ** 2
        j += 1
    if sum_c < ans:
        ans = sum_c
    i += 1
print(ans)