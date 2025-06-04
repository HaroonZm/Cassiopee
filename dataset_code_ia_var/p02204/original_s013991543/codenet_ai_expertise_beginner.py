m, n = input().split()
m = int(m)
n = int(n)
a = input().split()
for i in range(n):
    a[i] = int(a[i])

if m == 2:
    ans1 = 0
    for i in range(n):
        if (i % 2) != (a[i] % 2):
            ans1 = ans1 + 1
    ans2 = 0
    for i in range(n):
        if (i % 2) == (a[i] % 2):
            ans2 = ans2 + 1
    if ans1 < ans2:
        print(ans1)
    else:
        print(ans2)
else:
    ans = 0
    i = 0
    while i < n - 1:
        if a[i] == a[i+1]:
            a[i+1] = -1
            ans = ans + 1
        i = i + 1
    print(ans)