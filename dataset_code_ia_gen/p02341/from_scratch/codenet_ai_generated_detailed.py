MOD = 10**9 + 7

def number_of_ways(n, k):
    """
    Calcule le nombre de façons de placer n boules indistinguables dans k boîtes
    indistinguables, avec la contrainte qu'au maximum une boule par boîte.

    Analyse du problème :
    - Les boules sont indistinguables.
    - Les boîtes sont indistinguables.
    - Chaque boîte contient au plus une boule.
    - On doit placer toutes les boules.

    Conséquences:
    Comme chaque boîte peut contenir au plus une boule,
    et on a n boules, il faut au moins n boîtes (k >= n),
    sinon aucune solution.

    Puisque les boîtes sont indistinguables, la disposition ne dépend que du nombre de boîtes utilisées.
    Placer n boules dans k boîtes indistinguables et avec au plus une boule par boîte revient
    à sélectionner un ensemble de n boîtes parmi k, mais comme les boîtes sont indistinguables,
    les différentes affectations ne sont pas distinguées.

    En fait, comme boîtes sont indistinguables, seule la taille de la configuration compte.

    Avec n boules à mettre dans k boîtes, au plus une boule par boîte,
    les configurations distinctes correspondent au choix de n boîtes pour contenir les boules.

    Mais les boîtes étant indistinguables, il n'y a qu'une seule façon de répartir les boules dans les boîtes:
    * Soit k >= n, alors il y a 1 seule configuration : n boîtes contiennent chacune une boule, et les k-n boîtes sont vides (car indistinguables, on peut considérer que seules les boîtes occupées comptent).
    * Sinon 0 façons.

    Exemple:
    - Sample Input 1: 5 boules, 10 boîtes => k >= n donc 1 façon.
    - Sample Input 2: 200 boules, 100 boîtes => k < n donc 0 façon.

    Conclusion : le nombre de façons est 1 si n <= k, sinon 0.

    """
    if n <= k:
        return 1 % MOD
    else:
        return 0


# Lecture des entrées
n, k = map(int, input().split())

# Calcul et affichage du résultat modulo 10^9 + 7
print(number_of_ways(n, k))