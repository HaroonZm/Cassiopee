n = int(input())
numbers = input().split()
a = []
for i in range(n):
    a.append(int(numbers[i]))

cnt = 0
for i in range(n):
    min_index = i
    for j in range(i, n):
        if a[j] < a[min_index]:
            min_index = j
    temp = a[i]
    a[i] = a[min_index]
    a[min_index] = temp
    if i != min_index:
        cnt = cnt + 1

result = []
for i in range(n):
    result.append(str(a[i]))
print(" ".join(result))
print(cnt)