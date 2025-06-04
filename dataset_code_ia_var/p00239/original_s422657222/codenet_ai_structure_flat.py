while True:
    N = int(input())
    if N == 0:
        break
    line = []
    i = 0
    while i < N:
        line.append(input())
        i += 1
    PQRClist = input().split()
    P = int(PQRClist[0])
    Q = int(PQRClist[1])
    R = int(PQRClist[2])
    C = int(PQRClist[3])
    flag = False
    l = 0
    while l < N:
        item = line[l].split()
        s = int(item[0])
        p = int(item[1])
        q = int(item[2])
        r = int(item[3])
        if p <= P and q <= Q and r <= R and 4*p+9*q+4*r <= C:
            print(s)
            flag = True
        l += 1
    if not flag:
        print("NA")