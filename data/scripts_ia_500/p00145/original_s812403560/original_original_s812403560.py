n=int(input())
cards=[]
for i in range(n):
    a,b=map(int,input().split())
    cards.append((a,b))

memo=[[-1 for i in range(n+1)]for j in range(n+1)]
def getans (l,r,cards):
    if(memo[l][r]==-1):
        if(l+1==r):
            memo[l][r]=0
        else:
            ans=1<<32
            for m in range(l+1,r):
                cost=cards[l][0]*cards[m-1][1]*cards[m][0]*cards[r-1][1]+getans(l,m,cards)+getans(m,r,cards)
                ans=min(ans,cost)
            memo[l][r]=ans
    return memo[l][r]

print(getans(0,n,cards))