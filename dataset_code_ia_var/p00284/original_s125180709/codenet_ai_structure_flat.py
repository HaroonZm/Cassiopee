N = int(input())
i = 0
while i < N:
    s_d = input().split()
    s = int(s_d[0])
    d = int(s_d[1])
    s = s + 2**30
    d = d + 2**30
    ans = 0
    temp = s
    tempd = d
    while temp + (temp & -temp) <= tempd:
        temp = temp + (temp & -temp)
        ans = ans + 1
    tempd = tempd - temp
    while tempd:
        tempd = tempd - (tempd & -tempd)
        ans = ans + 1
    print(ans)
    i = i + 1