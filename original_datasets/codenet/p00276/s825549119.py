for i in range(int(input())):
    res = 0
    c,a,n = list(map(int,input().split()))
    res = min(n,a,c)
    c -= res
    a -= res
    if c >= 2 and a >= 1:
        cca = min(c//2,a)
        c -= cca*2
        res += cca

    if c >=3:
        res += c//3

    print(res)