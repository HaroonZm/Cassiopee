t = int(input())
for i in range(t):
    n, k  = map(int, input().split()) # n = len(xlist)
    xlist = list(map(int, input().split()))
    if (n <= k):
        print(0)
    else:
        betweenx = [xlist[i+1] - xlist[i] for i in range(n-1)]
        betweenx.sort()
        print(sum(betweenx[:n-k]))