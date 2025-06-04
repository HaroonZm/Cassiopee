from itertools import combinations

def calc_int(arr):
    """
    Calcule la représentation entière d'un ensemble de positions d'indices donnés, 
    en utilisant la somme des puissances de deux adéquates.
    
    Chaque indice i dans arr représente le bit i d'un entier mis à 1.
    Par exemple, si arr = [1, 3], la valeur retournée sera 2^1 + 2^3 = 2 + 8 = 10.
    
    Args:
        arr (Iterable[int]): Un itérable d'entiers représentant les indices à mettre à 1 dans l'entier résultant.
    
    Returns:
        int: L'entier dont les bits correspondant aux indices de arr sont mis à 1.
    """
    ret = 0
    # Pour chaque indice i, mettre à 1 le bit i dans ret (opération 1 << i)
    for i in arr:
        ret += 1 << i
    return ret

# Lecture de l'entrée utilisateur pour obtenir n et k 
n, k = map(int, input().split())

subsets = []  # Liste qui contiendra les tuples (valeur entière, sous-ensemble d'indices)

# Génération de tous les sous-ensembles de taille k parmi les n positions possibles
for sub in combinations(range(n), k):
    # Calcule la représentation entière de ce sous-ensemble
    subset_int = calc_int(sub)
    # Ajoute le tuple (valeur entière, sous-ensemble) à la liste
    subsets.append((subset_int, sub))

# Trie la liste des sous-ensembles selon leur représentation entière croissante
subsets.sort()

# Affichage formaté de chaque sous-ensemble et de sa représentation entière
for sub in subsets:
    # Si le sous-ensemble n'est pas vide, affiche les indices séparés par des espaces
    # Sinon, affiche uniquement la valeur entière suivie de ":"
    if len(sub[1]) != 0:
        print('{}: {}'.format(sub[0], ' '.join(map(str, sub[1]))))
    else:
        print(f'{sub[0]}:')