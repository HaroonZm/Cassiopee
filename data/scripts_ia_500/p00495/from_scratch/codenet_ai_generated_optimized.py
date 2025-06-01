A,B=map(int,input().split())
A_cards=list(map(int,input().split()))
B_cards=list(map(int,input().split()))
dp=[[0]*(B+1) for _ in range(A+1)]
max_len=0
for i in range(A-1,-1,-1):
    for j in range(B-1,-1,-1):
        if A_cards[i]==B_cards[j]:
            dp[i][j]=dp[i+1][j+1]+1
            if dp[i][j]>max_len:
                max_len=dp[i][j]
print(max_len)