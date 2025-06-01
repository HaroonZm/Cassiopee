n,m=map(int,input().split())
cards=[]
for _ in range(m):
    a,b=map(int,input().split())
    cards.append([a,b])
cards.sort(key=lambda x:x[0],reverse=True)
cost=0
for i in range(len(cards)-1):
    if cards[i][0]<n:
        cost+=n-cards[i][0]
print(cost)