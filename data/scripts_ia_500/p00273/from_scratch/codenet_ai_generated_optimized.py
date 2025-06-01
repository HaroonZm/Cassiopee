N=int(input())
for _ in range(N):
    x,y,b,p=map(int,input().split())
    min_cost=float('inf')
    for buy_b in range(b,7):
        for buy_p in range(p,7):
            cost=buy_b*x+buy_p*y
            if buy_b>=5 and buy_p>=2:
                cost=cost*0.8
            if cost<min_cost:
                min_cost=cost
    print(int(min_cost))