while True:
    n = int(input())
    if n == 0:
        break
    count = 0
    while count < n:
        data = input().split()
        a = int(data[0])
        b = int(data[1])
        c_ = int(data[2])
        d = int(data[3])
        e = int(data[4])
        f = int(data[5])
        g = int(data[6])
        h = int(data[7])
        c = a*e - b*f - c_*g - d*h
        i = a*f + b*e + c_*h - d*g
        j = a*g - b*h + c_*e + d*f
        k = a*h + b*g - c_*f + d*e
        print(c, i, j, k)
        count += 1