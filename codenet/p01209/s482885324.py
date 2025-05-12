import string

while(1):
    [N,M]=raw_input().split()
    N=int(N)
    if N==0: break
    S=string.digits+string.ascii_uppercase

    prime=[2,3,5,7,11,13,17,19,23,29,31]
    pc   =[0 for i in range(len(prime))]
    ans=999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
    for i in range(len(prime)):
        n=N
        while(1):
            if n%prime[i]==0:
                n/=prime[i]
                pc[i]+=1
            else:
                break
    L=0
    for i in range(1,len(M)+1):
        c=M[-i]
        L += S.index(c)*N**(i-1)
    
    for i in range(len(prime)):
        p=prime[i]
        if pc[i]!=0:
            k=1
            tmp=0
            while(p**k<=L):
                e=L/p**k
                tmp+= e
                k+=1
            tmp/=pc[i]
            ans=min(ans,tmp)
    print ans