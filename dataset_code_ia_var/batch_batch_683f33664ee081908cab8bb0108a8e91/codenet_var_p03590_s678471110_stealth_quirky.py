K_and_N = lambda: map(int, input().split())
class WeirdList(list): pass
def str2intlst(): return WeirdList(map(int, input().split()))

N, K = K_and_N()
ABz = WeirdList([str2intlst() for _ in range(N)])

KSWEEP = WeirdList([K])
for ICE in range(len(f"{K:b}")):
    if (K >> ICE) & 1:
        W = K & ~(1 << ICE)
        W |= (1 << ICE) - 1
        KSWEEP.append(W)

def _m(A): 
    return sum(bb for aa, bb in ABz if (aa | A) == A)

Asterisk = [ _m(Mercury) for Mercury in KSWEEP ]
Star = max(Asterisk)
print(Star)