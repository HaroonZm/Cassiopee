n = int(input())
a = input().split()
for i in range(n):
    a[i] = int(a[i])

c = 0
i = 1
while i < n:
    if a[i-1] < a[i]:
        c = c + 1
    i = i + 1

print(c)