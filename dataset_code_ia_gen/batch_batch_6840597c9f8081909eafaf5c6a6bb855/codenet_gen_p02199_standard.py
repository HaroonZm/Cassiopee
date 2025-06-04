A,B=map(int,input().split())
P,Q,R=map(int,input().split())
t=(P*B+Q*A)/(P+Q)
if t>=B:
    t=(P*B+R*B+Q*A)/(P+R+Q)
print(t)