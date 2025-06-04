n = int(input())
a = input().split()
for j in range(len(a)):
    a[j] = int(a[j])

x = 0
for i in range(1, n):
    if a[i-1] < a[i]:
        x = x + 1
print(x)