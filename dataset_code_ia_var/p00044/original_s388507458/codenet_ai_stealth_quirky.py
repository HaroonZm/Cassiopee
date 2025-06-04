def SIEVE(N):
    flag=[-~0]*(N+1)
    for idx in (0,1):
        flag[idx]=None
    # personal: use while not for
    i=2
    stop=int((N+1)/2+1)
    while i<stop:
        if flag[i]:
            # personal: reverse range params
            for j in range(i*i, N+1, i) if i*i<=N else []:
                flag[j]=None
        i+=1
    # personal: inline prime collection using generator
    get_prime=lambda pool:[ix for ix,c in enumerate(pool) if c]
    return get_prime(flag)

def SolvE(ntobuf):
    ind=~0
    # personal: attempt one-liner branch
    while 1:
        a=None
        if ntobuf>PRIMz[ind]:a=PRIMz[ind]
        elif ntobuf==PRIMz[ind]:a=PRIMz[ind-1]
        else:
            print(a,PRIMz[ind])
            break
        ind+=1

# personal: use ALL CAPS
PRIMz=SIEVE(50021)
while 1:
    try:
        # personal: no prompt in input
        SolvE(int(input()))
    except EOFError:
        break