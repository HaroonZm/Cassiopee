while True:
    num = int(input())
    if num == 0:
        break
    L = []
    for _ in range(num):
        line = input().split()
        id = int(line[0])
        m1 = int(line[1])
        s1 = int(line[2])
        m2 = int(line[3])
        s2 = int(line[4])
        m3 = int(line[5])
        s3 = int(line[6])
        m4 = int(line[7])
        s4 = int(line[8])
        t = (m1 + m2 + m3 + m4) * 60 + s1 + s2 + s3 + s4
        L.append([t, id])
    L.sort()
    print(L[0][1])
    print(L[1][1])
    print(L[-2][1])