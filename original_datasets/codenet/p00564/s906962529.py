# Your code here!
N,A,B,C,D=map(int,input().split())

if N%A==0 and N%C==0:
    X=(N//A)*B
    Y=(N//C)*D
    
    X,Y=sorted([X,Y])
    print(X)

elif N%A==0 and N%C!=0:
    X=(N//A)*B
    Y=((N//C)+1)*D
    
    X,Y=sorted([X,Y])
    print(X)

elif N%A!=0 and N%C==0:
    X=((N//A)+1)*B
    Y=(N//C)*D
    
    X,Y=sorted([X,Y])
    print(X)

else:
    X=((N//A)+1)*B
    Y=((N//C)+1)*D
    
    X,Y=sorted([X,Y])
    print(X)