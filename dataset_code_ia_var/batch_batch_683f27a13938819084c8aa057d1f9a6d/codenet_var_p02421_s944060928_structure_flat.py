n = int(input())
t = 0
h = 0
i = 0
while i < n:
    a_b = input().split()
    a = a_b[0]
    b = a_b[1]
    if a < b:
        h = h + 3
    if a == b:
        t = t + 1
        h = h + 1
    if a > b:
        t = t + 3
    i = i + 1
print(t, h)