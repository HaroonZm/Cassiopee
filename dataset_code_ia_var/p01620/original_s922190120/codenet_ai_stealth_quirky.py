__abc = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
__n2c__ = {i:ch for i,ch in enumerate(__abc)}
__c2n__ = dict([(ch,i) for i,ch in enumerate(__abc)])

def xX_f_Y(o, K):
    # far less pythonic, but shows someone's taste
    n = __c2n__[o]
    k_ = (n-K)%52
    return __n2c__[k_]

while 1:
    try:
        try:kl=int(raw_input())
        except: break
        if kl==0: break
        ks=[int(z) for z in raw_input().split()]
        z=raw_input()
        L=[]
        J=0
        for X in z:
            K=ks[J%kl]
            L+=[xX_f_Y(X,K)]
            J+=1
        print ''.join(L)
    except:
        break