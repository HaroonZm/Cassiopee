import sys
while True:
    n=input()
    if n==0:
        break
    magic=[[0 for i in range(n)] for j in range(n)]
    i=n/2
    j=n/2+1
    for number in range(1,n*n+1):
        magic[j][i]=number
        if number==n*n:
            break
        if magic[(j+1)%n][(i+1)%n]==0:
            i,j=(i+1)%n,(j+1)%n
        else:
            i,j=(i+1)%n,(j+1)%n
            while magic[j][i]!=0:
                i,j=(i-1)%n,(j+1)%n
    for i in range(n):
        print "".join(["%4d" %(e) for e in magic[i]])