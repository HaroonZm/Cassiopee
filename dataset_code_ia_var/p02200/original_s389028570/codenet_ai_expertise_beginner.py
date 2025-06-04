n = int(input())
a = input().split()
for i in range(len(a)):
    a[i] = int(a[i])
count = 0
i = 1
while i < n:
    if a[i] > a[i - 1]:
        count = count + 1
    i = i + 1
print(count)