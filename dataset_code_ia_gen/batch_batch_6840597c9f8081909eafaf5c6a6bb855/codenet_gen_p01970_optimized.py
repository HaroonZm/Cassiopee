import sys
input = sys.stdin.readline

MOD = 10**9 + 7
MAXQ = 10**6

# Crée une liste de booléens indiquant si un nombre est premier
is_prime = [True]*(MAXQ+1)
is_prime[0] = False
is_prime[1] = False
for i in range(2, int(MAXQ**0.5)+1):
    if is_prime[i]:
        for j in range(i*i, MAXQ+1, i):
            is_prime[j] = False

N = int(input())
qs = list(map(int, input().split()))

# Vérifier que la liste est strictement croissante (p1 < p2 < ... < pK)
# En principe, les produits sont triés par facteur premier (pas seulement croissants), donc on vérifie strictement < 
for i in range(1, N):
    if qs[i] <= qs[i-1]:
        print(0)
        sys.exit()

# Vérifier que tous les p_i sont premiers
for q in qs:
    if not is_prime[q]:
        print(0)
        sys.exit()

from collections import Counter

c = Counter(qs)
ans = 1
for freq in c.values():
    # Pour un facteur premier, fréquence = nombre d'apparitions dans l'affichage
    # Rappel : si exponent == 1, on affiche p_i une fois
    # Sinon on affiche p_i e_i fois
    # Le problème : une fréquence freq correspond à 1 occurrence d’exposant freq
    # Ou freq occurrences d’exposant 1 (mais par l’énoncé et l’ordre strict des p_i, ce n’est pas possible pour le même prime)
    # En fait, si un facteur premier p_i apparaît freq fois, c’est que son exposant est freq
    # Donc le nombre d’entrées d’entrée possibles est le nombre de manières d’attribuer l’exposant : exponent soit 1 (freq=1)->1 possibilité
    # Ou exponent= freq -> toujours 1 possibilité
    # Or le problème dit pour exposant=1, on affiche une fois p_i, pour exponent>1 on affiche p_i exponent fois.
    # Donc freq apparitions signifie son exposant vaut freq (freq >1) ou freq=1
    # Mais comme facteur premier unique, l’exposant est égal à freq
    # Le problème veut compter le nombre de M qui produisent cette sortie.
    # L’ambiguïté peut venir du réarrangement des facteurs avec exposants uniques et exposants multiples
    # Par exemple 2 3 3: 2^3 * 3^1 ou 2^1 * 3^3 sont possibles, donc 2 possibilités.
    # Donc on doit compter le nombre de façons de répartir les facteurs entre exposant 1 et exposant >1.
    # En d’autres termes, les facteurs qui apparaissent une seule fois ont exposant =1 forcément.
    # Ceux qui apparaissent plusieurs fois ont exposant = freq >1 ou peuvent être découper en plusieurs facteurs avec exposant 1 ? Non, les facteurs sont distincts.
    # Mais vu le problème, chaque groupe de facteurs identiques correspond à une exponentiation de ce facteur premier.
    # Donc chaque facteur premier correspond à un exposant = freq.
    # Dans le cas où freq=1, expo=1 donc une possibilité;
    # freq>1, expo= freq donc possibilité unique.
    # Or exemple input 1 montre 2 3 3 (freq(3)=2) donne 2 possibilités, pas 1.
    # Donc l’essentiel: s’il y a un facteur premier présent plus d’une fois, cela peut venir de 2 configurations:
    # - Ce facteur est à exposant freq (exposant>1)
    # - Ou ce facteur est exposant 1 répété freq fois, et un autre facteur est exposant freq
    # Dans l’exemple 2 3 3, ce sont 2 nombres:
    # (2^3)*3 et 2*(3^3), donc l’ambiguïté vient des facteurs qui apparaissent multiple fois.
    #
    # Le problème revient donc à compter le nombre de manières de partitionner les facteurs par valeurs uniques des facteurs.
    # En fait, pour les facteurs distincts (ils sont primes), compter combien de façons d’associer les puissances exponentielles telles que
    # l'affichage correspond.
    # La seule ambiguïté est quand un facteur premier apparaît plusieurs fois dans la sortie.
    # Deux options donc:
    # - ce facteur a un exposant égal au nombre d’apparitions (expo >1)
    # - ou ce facteur apparait une seule fois, et un autre facteur explose en un exposant egal à ce nombre
    #
    # En réalité le nombre correspond au nombre de façons de regrouper les facteurs identiques entre exposant unique et exposants multiple
    # En comptant les facteurs, chaque facteur premier apparaissant freq fois donne:
    # nombre de possibilités = 2^(freq-1)
    # Par exemple 2 3 3:
    # freq(2)=1 -> 1 possibilité
    # freq(3)=2 -> 2 possibilités (exposant 2 ou deux fois exposant 1)
    # total 1*2=2
    #
    # Pour 2 3 4 (3 facteurs: 2,3,4), 4 n’est pas premier -> 0 possibilités.
    # Pour 3 5 2: ordonnés 2 3 5, donc invalide car pq[i]<pq[i+1] n’est pas respecté -> 1 possibilité si trié.
    # Le problème dit que les facteurs dans la sortie sont triés, donc on peut supposer trois premier en ordre.
    #
    # En somme:
    # Le nombre de natural numbers = produit sur tous facteurs premiers de 2^(freq-1)
    # quand freq>0.
    #
    # Cependant, si freq=1, 2^(0) =1; si freq >1, 2^(freq-1).
    #
    # Donc on calcule cela.
    ans = (ans * pow(2, freq-1, MOD))%MOD

print(ans)