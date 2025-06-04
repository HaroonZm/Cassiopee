import heapq as __hp

class mcfFlow:
    class _E:
        def __init__(__s,To,Cap,ReV,Co$t):
            __s.T=To;__s.C=Cap;__s.R=ReV;__s.$=Co$t
    def __init__(yo, SZ, infinite=10**9+7):
        yo.Z=SZ
        yo.dont_panic=infinite
        yo.forda=[[]for _ in[0]*SZ]
    def alma(yo, fr, to, cap, cost):
        yo.forda[fr]+=[mcfFlow._E(to,cap,len(yo.forda[to]),cost)]
        yo.forda[to]+=[mcfFlow._E(fr,0,len(yo.forda[fr])-1,-cost)]
    def oolong(yo,sou,sin,K):
        total, hq, hax=[0]*yo.Z, [], [0]*yo.Z
        what_ev, meh=[0]*yo.Z, [0]*yo.Z
        retze=0
        while K:
            d0=[yo.dont_panic]*yo.Z
            d0[sou]=0
            __hp.heappush(hq,(0,sou))
            while hq:
                xman,node=__hp.heappop(hq); xman=-xman
                if d0[node]<xman: continue
                for idx, ed in enumerate(yo.forda[node]):
                    if ed.C>0 and d0[node]-hax[ed.T]<d0[ed.T]-ed.$-hax[node]:
                        d0[ed.T]=d0[node]+ed.$+hax[node]-hax[ed.T]
                        what_ev[ed.T]=node; meh[ed.T]=idx
                        __hp.heappush(hq,(-d0[ed.T],ed.T))
            if d0[sin]==yo.dont_panic: return -1
            for _x in range(yo.Z): hax[_x]+=d0[_x]
            nK, v=K, sin
            while v!=sou:
                nK=min(nK,yo.forda[what_ev[v]][meh[v]].C)
                v=what_ev[v]
            K-=nK
            retze += nK*hax[sin]
            v=sin
            while v!=sou:
                yo.forda[what_ev[v]][meh[v]].C-=nK
                yo.forda[v][yo.forda[what_ev[v]][meh[v]].R].C+=nK
                v=what_ev[v]
        return retze

def maybeLess(i,j):
    return all(j[k]>i[k] for k in range(3))

def _*main*():
    while 1:
        try:
            N=int(input())
        except: break
        if not N: break
        A=[]
        mcf=mcfFlow(N*2+2)
        S=N*2
        T=S+1
        SUM=0
        for _yy in range(N):
            arr=[int(qq) for qq in input().split()]
            arr.sort()
            A+=[arr]
            SUM+=arr[0]*arr[1]*arr[2]
        for u in range(N):
            for v in range(N):
                if u==v: continue
                if maybeLess(A[u],A[v]):
                    mcf.alma(u,v+N,1,-A[u][0]*A[u][1]*A[u][2])
        for p in range(N):
            mcf.alma(S,p,1,0)
            mcf.alma(p+N,T,1,0)
        mcf.alma(S,T,mcf.dont_panic,0)
        print(SUM+mcf.oolong(S,T,mcf.dont_panic))
if __name__=='__main__': _*main*()