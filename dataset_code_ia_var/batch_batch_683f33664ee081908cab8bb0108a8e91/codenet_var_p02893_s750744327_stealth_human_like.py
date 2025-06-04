mod = 998244353
import collections

# Bon, on prend n
n = int(input())
x = input()
# Calcul initial - probablement ça sera modifié plus tard...
ans = (2 * n * (int(x, 2) + 1)) % mod

def make_divisors(n):
    # Renvoie tous les diviseurs de n, hmm
    lst = []
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            lst.append(i)
            # attention au carré parfait
            if i != n // i:
                lst.append(n // i)
    # Je veux les plus grands d'abord, c'est utile ensuite
    lst.sort(reverse=True)
    return lst

D = make_divisors(n)
CT = collections.defaultdict(int)

for d in D:
    # Pourquoi on saute les pairs et 1? Je ne sais pas, mais on continue comme l'auteur...
    if d == 1 or d % 2 == 0:
        continue
    k = n // d
    # Cycle truc: pas évident, faudrait vérifier :)
    try:
        y = (2 ** n - 2 ** k) // (2 ** k + 1)
    except:
        y = 0 # Bon, si ça explose, tant pis

    ct = ((int(x, 2) - y) // (y + 1)) + 1 if y + 1 else 0

    # Pour enlever les doublons, on check les diviseurs de k aussi
    Dk = make_divisors(k)
    for dk in Dk:
        if dk < k:
            ct -= CT[dk]
    CT[k] = ct

    # L'auteur fait (je crois) une correction ici, -2*(n-k) pour chaque truc de ce genre
    ans -= ct * 2 * (n - k)
    # allez savoir pourquoi!

# Croisons les doigts, c'est sûrement modulo le gros nombre habituel
print(ans % mod)