N,K=map(int,input().split())
a = input()
ans = (N-1)//(K-1)
if (N-1)%(K-1)!=0:
    ans+=1
print(ans)