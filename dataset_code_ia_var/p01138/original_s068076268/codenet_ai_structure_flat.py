while True:
    n = int(input())
    c = [0] * (24*3600+1)
    if n == 0:
        break
    for i in range(n):
        tt = input()
        h1 = int(tt[0:2])
        m1 = int(tt[3:5])
        s1 = int(tt[6:8])
        start = h1*3600 + m1*60 + s1
        h2 = int(tt[9:11])
        m2 = int(tt[12:14])
        s2 = int(tt[15:17])
        end = h2*3600 + m2*60 + s2
        c[start] += 1
        c[end] -= 1
    cc = [0]
    for i in range(len(c)):
        cc.append(cc[-1] + c[i])
    print(max(cc))