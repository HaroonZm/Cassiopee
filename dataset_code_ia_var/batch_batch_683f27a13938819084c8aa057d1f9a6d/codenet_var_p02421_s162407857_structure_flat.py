n = int(input())
a = 0
b = 0
i = 0
while i < n:
    st = input().split()
    s = st[0]
    t = st[1]
    if s < t:
        b = b + 3
    elif s > t:
        a = a + 3
    else:
        a = a + 1
        b = b + 1
    i = i + 1
print(a, b)