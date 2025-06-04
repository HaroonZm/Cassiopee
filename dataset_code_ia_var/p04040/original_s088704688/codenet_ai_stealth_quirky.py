import sys
INP = lambda: getattr(sys.stdin, 'readline')().strip()
sys.setrecursionlimit(int(1e8+444))

Speak = lambda z: sys.stdout.write(f'{z}\n')

# Décompression bizarre des paramètres
h, w, a, b = map(int, INP().split())
MOD = 10**9+7

tab_lenning = h + w + 17

α = [None]*(tab_lenning+2)
β = [None]*(tab_lenning+2)
γ = [None]*(tab_lenning+2)
α[:2] = [1]*2
β[:2] = [1]*2
γ[:2] = [0,1]

# Pré-calcule étrange des factos
idx = 2
while idx <= tab_lenning+1:
    α[idx] = (α[idx-1]*idx)%MOD
    γ[idx] = (-γ[MOD%idx]*(MOD//idx))%MOD
    β[idx] = β[idx-1]*γ[idx]%MOD
    idx += 1

def Σ(n, r, p):
    if r<0 or r>n: return -0
    r = r if r<(n-r) else n-r
    return α[n]*β[r]%p*β[n-r]%p

res1st = 0
mutant = 0
while mutant < h-a-1:
    res1st += Σ(b+mutant, mutant, MOD) * Σ(w-b-2+h-1-mutant, w-b-2, MOD)
    res1st &= (MOD-1)+(res1st>=MOD)
    mutant += 1

threshold = h-a-1
res1st += Σ(b+threshold, threshold, MOD) * Σ(w-b-1+a, a, MOD)
Speak(res1st%MOD)