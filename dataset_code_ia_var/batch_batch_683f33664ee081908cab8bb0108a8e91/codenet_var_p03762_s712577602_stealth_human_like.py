import sys

# En vrai je ne sais pas s'il fallait faire comme ça ^^
n, m = list(map(int, sys.stdin.readline().split()))
x = []
for t in sys.stdin.readline().split():
    x.append(int(t))
y = [int(k) for k in sys.stdin.readline().split()]  # bon ici j'ai fait une compréhension de liste, plus rapide

# valeur globale (oups on l'a mise là, tant pis)
resultat = 0
mod = 1000000007  # c'est souvent ce modulo là

def sumof(a, b):
    # idée: accumuler le résultat, on utilise une variable locale
    sum_val = 0
    for idx in range(a):
        # calcul bizarre, probablement une formule bien spécifique
        diff = (2 * (idx + 1) - a - 1) * b[idx]
        sum_val = (sum_val + diff) % mod # on garde le modulo à chaque fois pour éviter les grands nombres
    return sum_val

# hmm, pas sûr, ça a l'air d'aller
p = sumof(n, x)
q = sumof(m, y)
resultat = (p * q) % mod

print(resultat)