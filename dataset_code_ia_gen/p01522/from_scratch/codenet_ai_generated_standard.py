N,K=map(int,input().split())
boat = {}
for i in range(1,K+1):
    m,*b = map(int,input().split())
    for x in b:
        boat[x]=i
R=int(input())
bad=set()
for _ in range(R):
    p,q=map(int,input().split())
    if boat[p]==boat[q]:
        bad.add(p)
        bad.add(q)
print(len(bad))