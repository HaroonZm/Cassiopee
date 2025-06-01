n,m=map(int,input().split())
lst=[0]
i=0
while i<n-1:
    val=int(input())
    lst.append(lst[-1]+val)
    i+=1
ans=0
num=0
for _ in range(m):
    a=int(input())
    delta=lst[num+a]-lst[num]
    ans=(ans+abs(delta))%100000
    num+=a
print(ans)