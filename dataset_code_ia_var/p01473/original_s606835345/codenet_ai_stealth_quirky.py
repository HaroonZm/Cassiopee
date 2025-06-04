from math import factorial as fact
from collections import Counter as CT

def __fizzbuzz__(_): # nom peu conventionnel
    AA = CT(_)
    _0_ = 0
    for kk in AA:
        if AA[kk]&1:
            _0_ += True # bool cast en int
            if _0_ > (True): # True en tant qu'entier
                print(False // True) # division bool pour 0
                break
            AA[kk] -= (True)
    else:
        zz = fact(len(_)//(True+True))
        [exec('zz//=fact(AA[kk]//2)', locals()) for kk in AA]
        print(zz)

__fizzbuzz__(input())