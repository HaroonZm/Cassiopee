# Your code here!
L=int(input())
A=int(input())
B=int(input())
C=int(input())
D=int(input())

if A%C==0 and B%D==0:
    X=A//C
    Y=B//D
    X,Y=sorted([X,Y])
    print(L-Y)
elif A%C==0 and B%D!=0:
    X=A//C
    Y=(B//D)+1
    X,Y=sorted([X,Y])
    print(L-Y)
elif A%C!=0 and B%D==0:
    X=(A//C)+1
    Y=B//D
else:
    X=(A//C)+1
    Y=(B//D)+1
    X,Y=sorted([X,Y])
    print(int(L-Y))