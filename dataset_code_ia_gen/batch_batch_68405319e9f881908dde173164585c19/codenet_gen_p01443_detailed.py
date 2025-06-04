import sys

# Cette fonction calcule (base^exp) % mod de manière efficace par exponentiation rapide
def mod_exp(base, exp, mod):
    result = 1
    cur = base % mod
    while exp > 0:
        if exp & 1:
            result = (result * cur) % mod
        cur = (cur * cur) % mod
        exp >>= 1
    return result

# Fonction principale qui pour un ensemble de nombres entiers [A, B],
# compte le nombre de sous-ensembles non vides qui sont triés à la fois
# par ordre numérique et par ordre lexicographique sur leur représentation en chaîne.
def count_sorted_subsets(A, B, P):
    # Générer la liste des entiers entre A et B
    numbers = list(range(A, B + 1))
    n = len(numbers)
    
    # Convertir en chaînes pour la comparaison lexicographique
    str_numbers = [str(x) for x in numbers]
    
    # Trier numériquement (croissant)
    num_sorted = sorted(numbers)
    # Trier lexicographiquement
    lex_sorted = sorted(numbers, key=lambda x: str(x))
    
    # Vérifier pour chaque nombre si la position dans les deux tris est la même.
    # Cette condition équivaut à la propriété suivante:
    # Pour tout couple (x,y), x<y numérique implique str(x)<str(y) lexicographiquement.
    # Donc argsort des deux tris doit être identique.
    # Nous allons construire un tableau où res[i]=1 si num_sorted[i] 
    # et lex_sorted[i] correspondent (même valeur).
    # Si res[i]=1 pour tous i, alors tout l'ensemble est bon.
    # Le problème demande les sous-ensembles, 
    # or à partir de l'ensemble complet, seuls des "blocs" contigus selon l'ordre lex
    # et numérique sont compatibles.
    # Examinons les permutations pour trouver les "blocs" de concordance.

    # On crée un dictionnaire position dans le tri lex
    pos_lex = {}
    for idx, val in enumerate(lex_sorted):
        pos_lex[val] = idx
    
    # On va examiner la permutation induced par les positions lex dans l'ordre numérique
    perm = [pos_lex[val] for val in num_sorted]
    # perm est une permutation de [0, n-1]
    
    # Nous cherchons les plus longs segments où perm[i] == i,
    # cela correspond aux sous-ensembles où
    # l'ordre numérique et lexicographique coïncident.
    # Or notre problème est plus fin, car les sous-ensembles peuvent
    # être n'importe quelles combinaisons des éléments pour lesquels la double
    # condition est vraie, mais seulement si dans la sous-liste triée numériquement,
    # la correspondance lex et numérique coïncide.

    # Le problème revient à: compter les sous-ensemble non vides
    # d'éléments qui forment des segments contigus dans num_sorted dans lesquels
    # perm[i]=i pour tous les éléments du segment.
    # En effet, si l'ordre de position lex est identique à l'ordre numérique
    # pour tous les éléments du segment, alors pour tout sous-ensemble de ce
    # segment, la propriété est vérifiée.
    
    # Ainsi, le tableau perm définit des positions,
    # et on détecte les segments continues où perm[i] == i.
    
    # Nous allons identifier ces "blocs" de longueur consécutive 
    # où perm[i] == i.
    
    total_subsets = 0
    
    # On parcourt perm et compte les longueurs de segments consécutifs perm[i]==i
    # pour chacun on ajoute (2^length -1) car toutes les combinaisons non vides
    # dans ce segment sont valides.
    
    length = 0
    for i in range(n):
        if perm[i] == i:
            length += 1
        else:
            # Si la chaine s'interrompt, on calcule les subsets pour le segment précédent
            if length > 0:
                total_subsets = (total_subsets + mod_exp(2, length, P) - 1) % P
                length = 0
    # Traiter le dernier segment s'il existe
    if length > 0:
        total_subsets = (total_subsets + mod_exp(2, length, P) - 1) % P

    return total_subsets % P

# Lire les données jusqu'à "0 0 0"
for line in sys.stdin:
    A, B, P = map(int, line.split())
    if A == 0 and B == 0 and P == 0:
        break
    result = count_sorted_subsets(A, B, P)
    print(result)