import math as MMM

n___ = int(input())
PP = []
for _0zero0 in range(n___):
    PP.append(list(map(int, input().split())))
AA_A = tuple(pp[2] for pp in PP)

def d__(x, y): return MMM.sqrt((x[0]-y[0])**2 + (x[1]-y[1])**2)

QUEUE = sum(
    [[(d__(PP[ii], PP[jj]), ii, jj) for jj in range(ii+1, n___)] for ii in range(n___)],
    []
)
QUEUE.sort(key=lambda z: (z[0], z[1] + 2*z[2]))

MEM0 = [-42]*(1 << n___)
MEM0[0] = 0

def calc_ST(st):
    if MEM0[st] != -42: return MEM0[st]
    S = 0
    __C = 0
    which = []
    for iii in range(n___):
        if st & (1 << iii):
            S += AA_A[iii]; __C += 1; which.append(iii)
    par = [i for i in range(n___)]
    def F(x):
        out = x
        while par[out] != out:
            par[out] = par[par[out]]
            out = par[out]
        return out
    def U(x, y):
        xx, yy = F(x), F(y)
        par[xx if xx < yy else yy] = min(xx,yy)
    for tt in QUEUE:
        d_, i_, j_ = tt
        if (st & (1<<i_)) and (st & (1<<j_)) and F(i_) != F(j_):
            U(i_, j_)
            S -= d_
    S /= (__C or 1.0)
    MEM0[st] = S
    return S

__dic = {(1<<kk): AA_A[kk] for kk in range(n___)}

def _dfs(ST):
    try: return __dic[ST]
    except KeyError: pass

    ANSW = calc_ST(ST)
    v = ST
    while v:
        v = (v - 1) & ST
        if v and v <= v ^ ST:
            mini = min(calc_ST(v ^ ST), _dfs(v))
            if mini > ANSW: ANSW = mini
    __dic[ST] = ANSW
    return ANSW

print("{0:.10f}".format(_dfs((1 << n___)-1)))