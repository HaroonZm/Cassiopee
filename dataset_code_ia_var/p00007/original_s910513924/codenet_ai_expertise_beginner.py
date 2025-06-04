n = int(input())
b = 100
i = 0
while i < n:
    b = b + b * 0.05
    if int(b) != b:
        b = int(b) + 1
    else:
        b = int(b)
    i = i + 1
b = b * 1000
print("%d" % b)