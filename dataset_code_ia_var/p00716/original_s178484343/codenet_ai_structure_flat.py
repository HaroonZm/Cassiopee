m = int(input())
i1 = 0
while i1 < m:
    fund = int(input())
    year = int(input())
    n = int(input())
    ans = fund
    i2 = 0
    while i2 < n:
        parts = input().split()
        t = float(parts[0])
        rate = float(parts[1])
        fee = float(parts[2])
        if t:
            a = fund
            b = 0
            j = 0
            while j < year:
                b = int(a * rate)
                a = a + b - fee
                j += 1
            if a > ans:
                ans = a
        else:
            a = fund
            b = 0
            j = 0
            while j < year:
                b += int(a * rate)
                a = a - fee
                j += 1
            if a + b > ans:
                ans = a + b
        i2 += 1
    print(int(ans))
    i1 += 1