N,A,B=map(int,input().split())
cnt=0
for i in range(N):
    n=int(input())
    if n<A or B<=n:
        cnt+=1
print(cnt)