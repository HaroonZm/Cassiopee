t = int(input())
for i in range(t):
    nk = input().split()
    n = int(nk[0])
    k = int(nk[1])
    x_input = input().split()
    xlist = []
    for x in x_input:
        xlist.append(int(x))
    if n <= k:
        print(0)
    else:
        betweenx = []
        for j in range(n-1):
            diff = xlist[j+1] - xlist[j]
            betweenx.append(diff)
        betweenx.sort()
        result = 0
        for h in range(n - k):
            result = result + betweenx[h]
        print(result)