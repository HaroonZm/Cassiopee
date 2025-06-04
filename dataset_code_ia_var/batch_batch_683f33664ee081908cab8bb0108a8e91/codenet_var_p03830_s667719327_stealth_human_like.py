import collections

# Fonction pour trouver les facteurs premiers
def primefactor(num):
    d = collections.defaultdict(int)
    for i in range(2, int(num ** .5)+1): # racine carrée suffit
        while num % i == 0:
            d[i] += 1
            num = num // i
    if num != 1: # dernier facteur si jamais
        d[num] += 1
    return d

# On lit l'entrée standard
n = int(input())
mod = 1000000007
res = 1
(cnt) = collections.defaultdict(int)
for i in range(1, n+1):
    pf = primefactor(i)
    for key in pf: # On ajoute la puissance de chaque facteur
        cnt[key] += pf[key]
for key in cnt:
    res = (res * ((cnt[key])+1))%mod # On multiplie (expo+1)
print(res)