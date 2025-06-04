n = int(input())
a = input().split()
for i in range(len(a)):
    a[i] = int(a[i])
ans = 0
i = 0
while i < n:
    if a[i] % 2 == 1:
        ans = ans + 1
    i = i + 2
print(ans)