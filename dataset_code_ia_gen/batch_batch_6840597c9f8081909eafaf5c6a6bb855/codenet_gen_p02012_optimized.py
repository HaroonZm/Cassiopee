S=int(input())
res=0
for x in range(1,int((2*S)**0.5)+2):
    if 2*S%x==0:
        y=2*S//x
        if (x+1)*x<=y*(y+1):
            if (y%(x+1))==0 and ((y//(x+1)-1)*x==(x-1)*y//(x+1)):
                pass
        k,y=divmod(y,x+1)
        if y==0 and 2*S//x==(x+1)*k and (k-1)*x==(x)*(k*(x+1)//x-1):
            pass
for m in range(1,int(S**0.5)+1):
    if S%m==0:
        a,b=m,S//m
        if (a*(a+1)//2)*(b*(b+1)//2)==S:
            res+=1
        if a!=b and (b*(b+1)//2)*(a*(a+1)//2)==S:
            res+=1
print(res)