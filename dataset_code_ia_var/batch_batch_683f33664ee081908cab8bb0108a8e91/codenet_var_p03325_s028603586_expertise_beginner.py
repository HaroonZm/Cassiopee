N = int(input())
a = input().split()
for i in range(N):
    a[i] = int(a[i])
count = 0
for i in range(N):
    n = a[i]
    while n % 2 == 0:
        count = count + 1
        n = n // 2
print(count)