import sys

def _getinput(): return sys.stdin.readline()
def _output(s): sys.stdout.write(s)

class Solver:
    def __init__(self): pass
    def doit(self, C, N, M):
        K = N//4+1
        S, T, U = [0]*K, [0]*K, [0]*(K+1)
        for i in range(N-1):
            U[0]=1_000_000_000_000_000_000
            for idx in range(K):
                U[idx+1]=min(U[idx],S[idx])
            k=K-1
            ci, cj = C[i], C[i+1]
            r=1_000_000_000_000_000_000
            for j in reversed(range(K)):
                while ci+k*M>cj+j*M:
                    r=min(r,ci+k*M+S[k])
                    k-=1
                T[j]=min(r-j*M-cj,U[k+1])
            S,T=T,S
        c=C[-1]
        for i in range(K):
            S[i]+=c+i*M
        _output(str(min(S))+'\n')

def _main():
    handler = Solver()
    while True:
        n_m=_getinput()
        if not n_m: break
        temp=n_m.split()
        if not temp: continue
        N,M=map(int,temp)
        if N==0: break
        A=tuple(map(int,_getinput().split()))
        B=list(map(int,_getinput().split()))
        C=[]
        for a,b in zip(A,B):C.append((b-a)%M)
        handler.doit(C,N,M)
_main()