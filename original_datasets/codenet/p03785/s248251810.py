import sys
def input(): return sys.stdin.readline().strip()
def mp(): return map(int,input().split())
def lmp(): return list(map(int,input().split()))

n,c,k=mp()
t=sorted([int(input()) for i in range(n)])
count=1
f=t[0]
ans=1
for i in range(1,n):
    count+=1
    d=t[i]-f
    if d>k or count>c:
        ans+=1
        count=1
        f=t[i]

print(ans)