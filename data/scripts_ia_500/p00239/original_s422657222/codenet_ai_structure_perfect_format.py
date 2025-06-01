while True:
    N = int(input())
    if N == 0:
        break
    line = []
    for l in range(N):
        line.append(input())
    P, Q, R, C = [int(i) for i in input().split()]
    flag = False
    for l in range(N):
        s, p, q, r = [int(i) for i in line[l].split()]
        if p <= P and q <= Q and r <= R and 4 * p + 9 * q + 4 * r <= C:
            print(s)
            flag = True
    if flag == False:
        print("NA")