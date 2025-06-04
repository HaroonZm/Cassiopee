a = input()
b = 0
i = 1
while i < len(a):
    if a[i] != a[i-1]:
        b = b + 1
    i = i + 1
print(b)