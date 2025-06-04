n = int(input())
a = list(map(int, input().split()))
for i in range(len(a)):
    for j in range(i + 1, len(a)):
        if a[i] > a[j]:
            a[i], a[j] = a[j], a[i]
b = []
i = 0
while i < len(a):
    b.append(a[i])
    i += 2
s = 0
for x in b:
    s += x
print(s)