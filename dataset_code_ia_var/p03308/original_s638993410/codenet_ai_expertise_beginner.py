n = int(input())
a = input().split()
for i in range(len(a)):
    a[i] = int(a[i])

min_a = a[0]
max_a = a[0]

for i in a:
    if i < min_a:
        min_a = i
    if i > max_a:
        max_a = i

print(max_a - min_a)