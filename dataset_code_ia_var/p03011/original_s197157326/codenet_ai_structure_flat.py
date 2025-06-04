a = input().split()
for i in range(len(a)):
    a[i] = int(a[i])
for i in range(len(a)):
    for j in range(i + 1, len(a)):
        if a[i] > a[j]:
            tmp = a[i]
            a[i] = a[j]
            a[j] = tmp
print(a[0] + a[1])