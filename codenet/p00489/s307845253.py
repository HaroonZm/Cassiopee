n=input()
l=[0]*(n+1)
for i in range(n*(n-1)/2):
    a,b,c,d=map(int,raw_input().split())
    if c>d:l[a]+=3
    if c<d:l[b]+=3
    if c==d:
    	l[a]+=1
        l[b]+=1
for i in range(1,n+1):
    x=1
    for j in range(1,n+1):
        if l[i]<l[j]:x+=1
    print x