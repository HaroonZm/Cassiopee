n=int(input())
A=list(map(int,input().split()))
q=int(input())
Ms=list(map(int,input().split()))
max_sum=sum(A)
dp=[False]*(max_sum+1)
dp[0]=True
for x in A:
    for s in range(max_sum,x-1,-1):
        if dp[s-x]:
            dp[s]=True
for M in Ms:
    print("yes" if M<=max_sum and dp[M] else "no")