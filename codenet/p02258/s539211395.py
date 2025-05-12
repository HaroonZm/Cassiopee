N = int(input())
R = [int(input()) for _ in range(N)]
maxi = -(10**10)
mini = R[0]
for i in range(1,N):
    maxi = max(maxi,R[i]-mini)
    mini = min(mini,R[i])
print(maxi)