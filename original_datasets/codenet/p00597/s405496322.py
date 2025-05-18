while(1):
    try:
        n=int(raw_input())
        if n==1:
            print 1
        else:
            A=[0 for i in range(n/2)]
            A[0]=1
            for i in range(1,n/2):
                A[i]=1+sum(A[:i])*2
            ans=sum(A)*2
            if n%2:
                ans+=1+sum(A)*2
            print ans
            
    except:
        break