while 1:
    n = int(input())
    if n == 0:
        break
    a = []
    i = 0
    while i < n:
        a.append(int(input()))
        i += 1
    temp = 0
    most = -999999999
    i = 0
    while i < n:
        temp = 0
        j = i
        while j < n:
            temp += a[j]
            if temp > most:
                most = temp
            j += 1
        i += 1
    print(most)