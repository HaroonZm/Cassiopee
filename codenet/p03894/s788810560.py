n,q=map(int,raw_input().split())
exist=set([1])
cup=range(n+2)
now=1
exist.add(cup[now-1])
exist.add(cup[now+1])
for i in xrange(q):
    a,b=map(int,raw_input().split())
    if now==a:now=b
    elif now==b:now=a
    tmp=cup[a]
    cup[a]=cup[b]
    cup[b]=tmp
    exist.add(cup[now-1])
    exist.add(cup[now+1])
exist=list(exist)
ans=0
for i in xrange(len(exist)):
    if exist[i]!=0 and exist[i]!=n+1:ans+=1
print ans