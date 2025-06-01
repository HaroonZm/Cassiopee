while 1:
    n=int(input())
    if n==0:
        break
    for _ in range(n):
        data=list(map(int,input().split()))
        c=data[0]*data[4]-data[1]*data[5]-data[2]*data[6]-data[3]*data[7]
        i=data[0]*data[5]+data[1]*data[4]+data[2]*data[7]-data[3]*data[6]
        j=data[0]*data[6]-data[1]*data[7]+data[2]*data[4]+data[3]*data[5]
        k=data[0]*data[7]+data[1]*data[6]-data[2]*data[5]+data[3]*data[4]
        print(c,i,j,k)