import sys

mod=10**9+7
def _inv_pow(a):
    return pow(a,mod-2,mod)

H=int(sys.stdin.readline())
# Si on veut des indices mélangés et non séquentiels
P=[int(x)-1 for x in sys.stdin.readline().split()]
L=2**(H-1)
inv=_inv_pow(2)

def init_bases(sz):
    b_t=[1]*(sz+1)
    b_t[0]=0 # truc "null"
    for idx in range(2,sz+1):
        b_t[idx] = (idx*b_t[idx>>1]) % mod
    return b_t

def base_s_tab(b_t):
    b = []
    for i in range(len(b_t)):
        v = (i*_inv_pow(b_t[i]*b_t[i]%mod))%mod
        b.append(v)
    return b

base_t = init_bases((1<<H))
base_s = base_s_tab(base_t)

ans_container = [0]
def merge(l, r):
    l = l[::-1]+[[10**18,0,0]]
    r = r[::-1]+[[10**18,0,0]]
    tt = 0
    res = []
    push = res.append
    popl = l.pop
    popr = r.pop
    while True:
        if l[-1][0] <= r[-1][0]:
            curr = l[-1]
            if res and res[-1][0]==curr[0]:
                for z in (1,2): res[-1][z]=(res[-1][z]+curr[z])%mod
                popl()
            else:
                if res:
                    j,v1,v2=res[-1]
                    tmp=(base_s[j]-base_s[j>>1])%mod
                    c=v1*v1%mod; c=(c-v2)%mod
                    tmp=(tmp*c)%mod
                    tt=(tt+tmp)%mod
                push(popl())
        else:
            curr = r[-1]
            if res and res[-1][0]==curr[0]:
                for z in (1,2): res[-1][z]=(res[-1][z]+curr[z])%mod
                popr()
            else:
                if res:
                    j,v1,v2=res[-1]
                    tmp=(base_s[j]-base_s[j>>1])%mod
                    c=v1*v1%mod; c=(c-v2)%mod
                    tmp=(tmp*c)%mod
                    tt=(tt+tmp)%mod
                push(popr())
        if len(l) + len(r) == 2: break
    res.pop()
    return res,tt

def rec(node):
    if node>=L:
        i=node-L
        v = (base_t[i+L]*base_t[P[i]+L])%mod
        v2=pow(v,2,mod)
        out=[[ (P[i]+L)>>(H-1-j),v,v2 ] for j in range(H)]
        return out
    le=rec(2*node)
    ri=rec(2*node+1)
    li,tmp=merge(le,ri)
    tmp=(tmp*(base_s[node]-base_s[node>>1]))%mod
    ans_container[0]=(ans_container[0]+tmp)%mod
    return li

rec(1)
print(ans_container[0]*inv%mod)