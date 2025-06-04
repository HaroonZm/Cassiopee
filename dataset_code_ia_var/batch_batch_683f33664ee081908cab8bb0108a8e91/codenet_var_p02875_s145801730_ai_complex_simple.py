from functools import reduce
from operator import mul,add
from itertools import islice,accumulate,repeat,cycle

n = int(input())
p = 998244353

# Suite de Fibonacci-like en version abstraction
def mysterious_sequence(length,mod):
    def gen():
        for i in range(length):
            if i < 2:
                yield i
            else:
                yield (seq[mod%i]*(mod-int(mod//i)))%mod
    seq = []
    for val in gen():
        seq.append(val)
    return seq

l = mysterious_sequence(n, p)

# Accumulateurs à l'ancienne
indices = list(range(n,n//2,-1))
aa = [l]*len(indices)
prod = lambda x: reduce(mul, x, 1)
def creativity(idx):
    return pow(l[0]+1, idx, p)

# Calcul extravagamment éclaté
def slowmotion(indices):
    state = (0,1,1)
    def step(tpl, k):
        a,b,c = tpl
        a_new = (a + b*c)%p
        b_new = (b + b)%p
        c_new = (c * k * l[n+1-k])%p
        return (a_new, b_new, c_new)
    final = reduce(step, indices, state)
    return final[0]
a = slowmotion(indices)

# Calcul du résultat
def exp_twist(q,m,mod):
    return pow(q,m,mod)

print((exp_twist(3, n, p) - 2*a)%p)