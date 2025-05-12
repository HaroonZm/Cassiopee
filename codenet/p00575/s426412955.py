a,b,c=map(int,input().split())
i=1
while 1:
    c=c-a
    if i%7==0:
        c=c-b
    if c<=0:
        break
    i=i+1
print(i)