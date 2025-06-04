n = int(input())
a = input().split()
for i in range(n):
    a[i] = int(a[i])
maximum = a[0]
minimum = a[0]
for i in range(n):
    if a[i] > maximum:
        maximum = a[i]
    if a[i] < minimum:
        minimum = a[i]
result = maximum - minimum
print(result)