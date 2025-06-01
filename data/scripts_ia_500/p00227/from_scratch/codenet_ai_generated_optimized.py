while True:
    n,m=map(int,input().split())
    if n==0 and m==0:
        break
    prices=list(map(int,input().split()))
    prices.sort(reverse=True)
    total=sum(prices)
    for i in range(m-1,len(prices),m):
        total-=prices[i]
    print(total)