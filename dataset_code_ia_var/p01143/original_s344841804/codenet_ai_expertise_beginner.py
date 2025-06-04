while True:
    nmp = input().split()
    n = int(nmp[0])
    m = int(nmp[1])
    p = int(nmp[2])
    if n == 0 and m == 0 and p == 0:
        break
    x = []
    for i in range(n):
        xi = int(input())
        x.append(xi)
    if x[m-1] == 0:
        print(0)
    else:
        total = 0
        for val in x:
            total += val
        res = int(total * (100 - p) / x[m-1])
        print(res)