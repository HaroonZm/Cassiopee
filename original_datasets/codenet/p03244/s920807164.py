from collections import Counter
n=int(input())
v=list(map(int,input().split()))
v1=v[0:n:2]
v2=v[1:n:2]
cc1=Counter(v1)
c1=cc1.most_common()
cc2=Counter(v2)
c2=cc2.most_common()
if c1[0][0]!=c2[0][0]:
    print(n-c1[0][1]-c2[0][1])
if c1[0][0]==c2[0][0]:
    if len(c1)==len(c2)==1:
        print(n//2)
    if len(c1)==1 and len(c2)!=1:
        print(n-c1[0][1]-c2[1][1])
    if len(c2)==1 and len(c1)!=1:
        print(n-c1[1][1]-c2[0][1])    
    if len(c1)>1 and len(c2)>1:    
        print(n-max(c1[1][1]+c2[0][1],c1[0][1]+c2[1][1]))