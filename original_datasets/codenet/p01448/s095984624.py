import itertools
n=int(input())
table=[0 for i in range(100003)]
table[0]=1
for i in range(n):
    a,b=map(int,input().split())
    table[a]+=1
    table[b+1]-=1
table=list(itertools.accumulate(table))
for i in range(len(table)):
    if table[i]>=i:
        ans=i
print(ans-1)