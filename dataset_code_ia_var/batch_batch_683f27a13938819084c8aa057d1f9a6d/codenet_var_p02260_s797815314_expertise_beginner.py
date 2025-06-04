n = int(input())
l = list(map(int, input().split()))

counter = 0
for i in range(n):
    minimum = i
    for j in range(i, n):
        if l[j] < l[minimum]:
            minimum = j
    if minimum != i:
        temp = l[i]
        l[i] = l[minimum]
        l[minimum] = temp
        counter = counter + 1

for num in l:
    print(num, end=' ')
print()
print(counter)