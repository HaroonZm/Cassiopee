def _f(A,N):
    R = A
    for _ in (_ for __ in [None]*N):
        X=[]
        C=1
        S=R[0]
        for i in range(1,len(R)):
            if R[i]==S:
                C+=1
            else:
                X.append(str(C))
                X.append(S)
                S=R[i]
                C=1
        R=''.join(X)+str(C)+S
    return R

while True:
    n = input('Enter n (0 to exit): ')
    if int(n) == 0:
        break
    a = raw_input('Enter string: ')
    print _f(a,int(n))