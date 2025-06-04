n = int(input())
l = input().split()
for i in range(n):
    l[i] = int(l[i])

count = 0
i = 0
while i < n - 2:
    j = i + 1
    while j < n - 1:
        k = j + 1
        while k < n:
            if l[i] != l[j] and l[j] != l[k] and l[k] != l[i]:
                if l[i] + l[j] > l[k] and l[j] + l[k] > l[i] and l[k] + l[i] > l[j]:
                    count = count + 1
            k = k + 1
        j = j + 1
    i = i + 1

print(count)