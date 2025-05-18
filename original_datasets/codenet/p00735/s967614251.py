S = [0 for i in range(300000)]
S2 = []
A = [-1, 1]
for i in range(1, int(300000 / 7) + 1):
    d = 7 * i
    for a in A:
        da = d + a
        if da < 300000 and S[da] == 0:
            S2.append(da)
            for j in range(2, int(300000 / 2)):
                if da * j >= 300000:break
                S[da * j] = -1
while 1:
    n = int(input())
    if n == 1:break
    #res = [str(n) + ':']
    #res += [x for x in S2 if int(x) <= n and n % int(x) == 0]
    print(str(n) + ':',' '.join([str(x) for x in S2 if n % x == 0 and x <= n]))