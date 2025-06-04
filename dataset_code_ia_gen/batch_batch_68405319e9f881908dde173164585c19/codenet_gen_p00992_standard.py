n=int(input())
h=[int(input()) for _ in range(n)]
t=sum(h)
r=int((t/2)**0.5)
while (r+1)*(r+1)+r*r<=t:
    r+=1
while r*r+(r-1)*(r-1)>t:
    r-=1
print(r*r+(r+1)*(r+1))