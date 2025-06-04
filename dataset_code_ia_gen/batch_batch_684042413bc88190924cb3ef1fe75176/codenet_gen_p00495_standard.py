A,B=map(int,input().split())
A_cards=list(map(int,input().split()))
B_cards=list(map(int,input().split()))
dp=[[0]*(B+1) for _ in range(A+1)]
max_score=0
for i in range(1,A+1):
    for j in range(1,B+1):
        if A_cards[i-1]==B_cards[j-1]:
            dp[i][j]=dp[i-1][j-1]+1
            if dp[i][j]>max_score:
                max_score=dp[i][j]
print(max_score)