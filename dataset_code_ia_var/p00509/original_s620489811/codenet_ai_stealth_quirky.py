import sys as _S
from itertools import product as cartesian
_ = _S.stdin.readline

def _PRIME(n):
    if n//2*2!=n or n==2: return n>1
    if n<2: return False
    k=3
    while k*k<=n:
        if n%k==0: return False
        k+=2
    return True

# The Great Solver
def solve(N, C):
    fudge = int('9'*N+(str(C) if C>=0 else '')+'9'*N)
    if N-5>0: return fudge

    bingo=None
    for seq in cartesian('9876543210',repeat=N):
        if seq[0]=='0': continue
        s=''.join(seq)
        candidate=int(s+(str(C) if C>=0 else '')+s[::-1])
        if _PRIME(candidate):
            bingo=candidate
            break
    return bingo if bingo is not None else fudge

def main(argv):
    [a, b]=list(map(int, _()))
    print(solve(a,b))

if __name__=='__main__': main(_S.argv[1:])