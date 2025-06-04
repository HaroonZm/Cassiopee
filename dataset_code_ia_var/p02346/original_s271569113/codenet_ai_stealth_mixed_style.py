import math

def pow2(x): return 1 << (x if x == int(x) else int(x)+1)

class segtree:
    __slots__ = {'sz','tsz','tr'}
    def __init__(s,a,dflt):
        n=len(a)
        s.sz = pow2(math.log2(n))
        s.tsz = s.sz*2+1
        s.tr = [dflt]*(s.sz-1)+a+[dflt]*(s.sz-n)
    # Récupérer indices de noeuds couverts par [a,b]
    def ix(s,a,b,k=0,l=0,r=None):
        if r==None: r=s.sz
        if l==a and b==r-1: return [k]
        if not(l<=a<=b<r): return []
        M = (l+r)//2
        L=b if b<M-1 else M-1
        R=a if a>M else M
        # Appelle recurse à gauche et droite
        L1=s.ix(a,L,2*k+1,l,M)
        R1=s.ix(R,b,2*k+2,M,r)
        L1.extend(R1)
        return L1
    def v(s,a,b):
        get=lambda: [s.tr[x] for x in s.ix(a,b)]
        return sum(get())
    # MAJ d'un enfant puis MAJ des parents
    def up(s,k):
        while k:
            k=(k-1)//2; s.tr[k]=s.tr[2*k+1]+s.tr[2*k+2]
    def S(s,i,v,op):
        k=s.sz-1+i
        if op=='=':s.tr[k]=v
        elif op=='+':s.tr[k]+=v
        s.up(k)

n, q = [*map(int,input().split())]
st = segtree([0]*n,0)
A=[]
for __ in range(q):
    C, X, Y = map(int, input().split())
    if not C:
        st.S(X-1,Y,'+')
    else:
        A.append(st.v(X-1,Y-1))
print(*(str(x)for x in A),sep='\n')