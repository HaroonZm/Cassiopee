n = int(input())
a, b = 0, 0
for i in range(n):
    s, t = input().split()
    if s < t:
        b += 3
    elif s > t:
        a += 3
    else:
        a += 1
        b += 1
print(a, b)