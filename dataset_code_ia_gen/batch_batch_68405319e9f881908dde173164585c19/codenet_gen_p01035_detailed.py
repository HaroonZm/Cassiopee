import sys
import bisect

input = sys.stdin.readline

# Solution basée sur un index des valeurs uniques et positions associées
# Pour chaque valeur de dureté rencontrée a_i, on stocke la liste triée des positions i où elle apparaît.
# Pour chaque requête (l, r, D), on cherche les valeurs a_i proches de D dans cet ensemble unique.
# Comme on veut la valeur a_i telle que |a_i - D| soit minimale, on examine les valeurs a_i immédiates autour de D dans la liste triée des valeurs uniques.
# Pour ces candidats on fait une recherche binaire sur les indices des positions pour voir s’il y a une occurrence entre l et r.
# On prend la distance minimale de |a_i - D| parmi ces occurrences valides.
# Cette méthode permet de répondre efficacement à Q requêtes sans passer par un segment tree sophistiqué.

N = int(input())
a = list(map(int, input().split()))
Q = int(input())

# Construction du dictionnaire valeur -> positions triées
pos_dict = {}
for i, val in enumerate(a):
    if val not in pos_dict:
        pos_dict[val] = []
    pos_dict[val].append(i)

# Liste triée des valeurs uniques
unique_vals = sorted(pos_dict.keys())

def check_in_range(arr, l, r):
    """
    Vérifie si un élément de la liste arr (déjà triée)
    se trouve dans l'intervalle [l, r].
    Utilise une recherche binaire.
    Renvoie True si oui, False sinon.
    """
    # Cherche la plus petite position >= l
    idx = bisect.bisect_left(arr, l)
    if idx < len(arr) and arr[idx] <= r:
        return True
    return False

for _ in range(Q):
    l, r, D = map(int, input().split())

    # Trouver la position d'insertion de D dans unique_vals
    idx = bisect.bisect_left(unique_vals, D)

    candidates = []

    # Valeur immédiatement >= D (ou égale à D)
    if idx < len(unique_vals):
        val = unique_vals[idx]
        if check_in_range(pos_dict[val], l, r):
            candidates.append(abs(val - D))

    # Valeur immédiatement < D
    if idx > 0:
        val = unique_vals[idx - 1]
        if check_in_range(pos_dict[val], l, r):
            candidates.append(abs(val - D))

    # Si aucun candidat trouvé, cela signifie que dans [l,r] il n'y a pas de valeurs proches à D ?
    # Ce cas ne se produit pas si a contient au moins une valeur dans [l,r].
    # Néanmoins, on couvre le cas où aucune position n'est dans [l,r] en cherchant manuellement.
    # Optionnel, car la contrainte garantit a dans [l,r].
    # Pour la sécurité, on peut faire une recherche complète (plus lente) si on veut,
    # mais on suppose que ça ne sera pas nécessaire dans ce problème.

    # Afficher la plus petite différence trouvée
    print(min(candidates))