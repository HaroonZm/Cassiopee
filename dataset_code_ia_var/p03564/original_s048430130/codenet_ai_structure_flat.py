n = int(input())
k = int(input())
x = 1
i = 0
while i < n:
    a = x * 2
    b = x + k
    if a < b:
        x = a
    else:
        x = b
    i += 1
print(x)