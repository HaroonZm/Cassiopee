while True:
    try:
        n = int(input())
    except:
        exit()
    a = input().split()
    for i in range(len(a)):
        a[i] = int(a[i])
    a.sort()
    i = 0
    while i < n - 1:
        a[i + 1] = a[i + 1] + a[i]
        i += 1
    s = 0
    j = 0
    while j < len(a):
        s += a[j]
        j += 1
    print(s)