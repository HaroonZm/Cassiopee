while True:
    n=int(input())
    if n==0:
        break
    elif n==1:
        print(1) 
    else:
        B=[0]*(n+1)
        B[0]=1
        B[1]=1
        B[2]=2
        for i in range(3, n+1):
            B[i]=B[i-1]+B[i-2]+B[i-3]
        if B[n]%3650==0:
            print(B[n]//3650)
        else:
            print(B[n]//3650+1)