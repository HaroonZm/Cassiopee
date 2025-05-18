while 1:
    N = int(input())
    if N == 0:
        break
    a = b = c = 0
    a0 = b0 = c0 = 0
    for i in range(N):
        s0, s1 = input().split()
        h, m = map(int, s0.split(":"))
        tm = 100*h + m
        m1 = int(s1)
        if m1 < m:
            m1 += 60
        if 1100 <= tm < 1500:
            if m1 - m <= 8:
                a += 1
            a0 += 1
        elif 1800 <= tm < 2100:
            if m1 - m <= 8:
                b += 1
            b0 += 1
        elif 2100 <= tm or tm < 200:
            if m1 - m <= 8:
                c += 1
            c0 += 1
    print("lunch", 100*a//a0 if a0 else "no guest")
    print("dinner", 100*b//b0 if b0 else "no guest")
    print("midnight", 100*c//c0 if c0 else "no guest")