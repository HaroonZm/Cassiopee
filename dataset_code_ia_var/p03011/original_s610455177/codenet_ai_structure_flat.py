a = input().split()
for i in range(len(a)):
    a[i] = int(a[i])
m = a[0]
for i in a:
    if i > m:
        m = i
for i in range(len(a)):
    if a[i] == m:
        del a[i]
        break
s = 0
for i in a:
    s += i
print(s)