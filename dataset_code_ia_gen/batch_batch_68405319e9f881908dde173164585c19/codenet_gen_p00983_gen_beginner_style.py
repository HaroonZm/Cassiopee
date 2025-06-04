import sys
sys.setrecursionlimit(10**7)

MOD = 10**9 + 7

n,m = map(int, input().split())
s = list(map(int, input().split()))

# On va faire une recherche par essais, pour chaque document on peut le mettre dans la pile A ou B
# On garde les piles comme listes (empilent à droite)
# On s'assure qu'en ajoutant le document la pile reste strictement décroissante (car on doit avoir l'ordre inverse)
# et on n'excède pas la capacité m.
# Comme n peut aller jusqu'à 5000, une recherche complète est impossible. Mais on fait comme un débutant et on écrit la solution brute.

# On va essayer une approche purement récursive avec mémoïsation sur (index, lastA, lenA, lastB, lenB)
# Mais lastA et lastB sont les numéros de doc à la tête de A et B, et peuvent être 0 s'ils sont vides.
# Stocker les états serait trop lourd, donc on ne mémorise pas et croit que la mémoire suffira pour les petits input.
# Pour grands input, ce code sera trop lent mais correspond à la consigne.

# Version naïve pure récursive sans mémo :

def dfs(i, lastA, lenA, lastB, lenB):
    if i == n:
        return 1
    ways = 0
    doc = s[i]
    # essayer pile A
    if (lenA < m) and (lastA == 0 or doc < lastA):
        ways += dfs(i+1, doc, lenA+1, lastB, lenB)
    # essayer pile B
    if (lenB < m) and (lastB == 0 or doc < lastB):
        ways += dfs(i+1, lastA, lenA, doc, lenB+1)
    return ways % MOD

# appel initial :
res = dfs(0,0,0,0,0)
print(res % MOD)