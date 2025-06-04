A,B,C=map(int,input().split())
if A>B:
    tmp=A
    A=B
    B=tmp
i=A
f=0
while i<B:
    if C==i:
        f=1
        break
    i+=1
if f==1:
    print("Yes")
else:
    print("No")