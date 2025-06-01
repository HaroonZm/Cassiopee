import sys
input=sys.stdin.readline
n=int(input())
d={}
for _ in range(n):
    p,c=input().split()
    d[p]=d.get(p,0)+int(c)
res=sorted(d.items(),key=lambda x:(len(x[0]),x[0]))
for k,v in res:
    print(k,v)