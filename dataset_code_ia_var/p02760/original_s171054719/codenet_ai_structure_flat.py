a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list(map(int, input().split()))
maru = 111
flag = 0
n = int(input())
k = 0
while k < n:
    e = int(input())
    i = 0
    while i < 3:
        if e == a[i]:
            a[i] = maru
        if e == b[i]:
            b[i] = maru
        if e == c[i]:
            c[i] = maru
        i += 1
    k += 1
j = 0
while j < 3:
    if a[j] == b[j] and b[j] == c[j]:
        if c[j] == maru:
            flag = 1
    j += 1
if a[0] == a[1] and a[1] == a[2]:
    if a[0] == maru:
        flag = 1
if b[0] == b[1] and b[1] == b[2]:
    if b[0] == maru:
        flag = 1
if c[0] == c[1] and c[1] == c[2]:
    if c[0] == maru:
        flag = 1
if a[0] == b[1] and b[1] == c[2]:
    if c[2] == maru:
        flag = 1
if a[2] == b[1] and b[1] == c[0]:
    if c[0] == maru:
        flag = 1
if flag == 1:
    print("Yes")
else:
    print("No")