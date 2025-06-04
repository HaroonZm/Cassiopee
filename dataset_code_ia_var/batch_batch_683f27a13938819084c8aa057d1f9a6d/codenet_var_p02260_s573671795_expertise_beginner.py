n = int(input())
a = input().split()
for i in range(n):
    a[i] = int(a[i])
cnt = 0
i = 0
while i < n:
    minj = i
    j = i
    while j < n:
        if a[j] < a[minj]:
            minj = j
        j = j + 1
    if i != minj:
        cnt = cnt + 1
    temp = a[i]
    a[i] = a[minj]
    a[minj] = temp
    i = i + 1

for num in a:
    print(num, end=" ")
print()
print(cnt)