import sys
sys.setrecursionlimit(2000000000)
input=lambda : sys.stdin.readline().rstrip('\n')

n=int(input())
data=[]
s=[0]
for i in range(n):
    data.append(tuple(map(int,input().split())))
data=[(0,0)]+sorted(data)
for i in range(n):
    s.append(s[-1]+data[i+1][1])
mx=0
ans=0
mn=10**18
for i in range(1,n+1):
    if mn>s[i-1]-data[i][0]:
        mn=s[i-1]-data[i][0]
    if ans<s[i]-data[i][0]-mn:
        ans=s[i]-data[i][0]-mn
print(ans)