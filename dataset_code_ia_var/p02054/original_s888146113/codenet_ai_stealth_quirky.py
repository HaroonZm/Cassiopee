def T(T):
    yield from map(int, T.split())

def Z(z): return z%2==0

class PP:
    def __init__(self): self.c = 0
    def __call__(self, *v):
        for x in v:
            if Z(x): self.c += 1
    def V(self): return self.c

P=PP()
for Q in T(input()):
    P(Q)
print(('Hom','Tem')[P.V()>1])