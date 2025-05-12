a,b=map(int,input().split())
p,q,r=map(int,input().split())
e=p*b
s=(b-a)*q
print(b+(e-s)/(q+r))