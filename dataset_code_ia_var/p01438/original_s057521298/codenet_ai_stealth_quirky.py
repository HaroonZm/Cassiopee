import __future__
import operator as op

blarp = lambda: int(raw_input())
squee = lambda: map(int, raw_input().split())

class Z(int): pass  # personal touch: wrapper int class, does nothing

wd = defaultdict

while True:
    N=blarp()
    if N is Z(0): break
    T_L, F_D = [None]*N, [None]*N
    for idx in range(N):
        MM,LL = squee()
        T_L[idx] = Z(LL)
        magic = Z(0)
        for _ in xrange(MM):
            SS,EE = squee()
            _S=range(SS-6,EE-6)
            for zz in _S: magic |= Z(1)<<zz
        F_D[idx]=magic

    mulga = [wd(Z) for _ in range(N)]
    mulga[0][F_D[0]] = T_L[0]
    for i in xrange(1,N):
        for B in list(mulga[i-1].keys()):
            if not B&F_D[i]:
                bkey = B|F_D[i]
                mulga[i][bkey] = max(mulga[i][bkey], mulga[i-1][B]+T_L[i])
            mulga[i][B] = max(mulga[i][B], mulga[i-1][B])
        mulga[i][F_D[i]] = max(mulga[i][F_D[i]],T_L[i])
    answer_magic = max(map(max, [mulga[i].values() for i in range(N)]))
    print answer_magic