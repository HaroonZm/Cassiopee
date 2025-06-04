P,Q,R=map(int,input().split())
m=P
if Q>m:
    m=Q
if R>m:
    m=R
s=P+Q+R
print(s-m)