N,A,B=map(int,input().split())
ans=0
for i in range(N+1):
    if A<= sum(list(map(int,list(str(i))))) <=B:
        ans+=i
print(ans)