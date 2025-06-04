a,b,c=map(int,input().split())
x=0
i=a
while i<=b:
    if c%i==0:
        x+=1
    i+=1
print(x)