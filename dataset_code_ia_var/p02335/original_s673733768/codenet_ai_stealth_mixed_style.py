from functools import reduce

class Solver:
    def __init__(self):
        self.MOD = int(1e9+7)
    def solve(self, N, K):
        if K<N:
            print(0)
            return
        # Utilisation de reduce pour le produit
        def f(a, b): return a*b % self.MOD
        p = 1
        for i in range(N):
            p = (p * (K-i)) % self.MOD
        # Approche fonctionnelle pour le dénominateur
        q = reduce(f, (x+1 for x in range(N)), 1)
        # Calcul via une expression lambda/mapping
        res = (lambda x, y: x * pow(y, self.MOD-2, self.MOD) % self.MOD)(p, q)
        print(res)
        
N_K = list(map(int, input().split()))
inst = Solver()
inst.solve(*N_K)