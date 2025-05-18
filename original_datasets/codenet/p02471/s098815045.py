#AOJのコース用からJOI2006用に編集

L=input().split( )
a=[int(L[0]),1,0]#gcd途中の余り、その余りをka+lbと表したk,l
b=[int(L[1]),0,1]

while a[0]%b[0]!=0:
    k=a[0]//b[0]

    c=b[0]
    c1=b[1]
    c2=b[2]

    a[1]-=(k*b[1])
    a[2]-=(k*b[2])

    b[0]=a[0]%b[0]
    b[1]=a[1]
    b[2]=a[2]

    a[0]=c
    a[1]=c1
    a[2]=c2
    #print(a,b)
k=a[0]//b[0]

c=b[0]
c1=b[1]
c2=b[2]

a[1]-=(k*b[1])
a[2]-=(k*b[2])

b[0]=a[0]%b[0]
b[1]=a[1]
b[2]=a[2]

a[0]=c
a[1]=c1
a[2]=c2
#print(a,b)
print(a[1],a[2])