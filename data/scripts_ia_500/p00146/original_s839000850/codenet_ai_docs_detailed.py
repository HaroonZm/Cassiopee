n = int(input())
ids = []
dists = []
weights = []

# Lecture des données d'entrée pour chaque élément
for _ in range(n):
    # Lecture des identifiants, distances et valeurs
    s, d, v = map(int, input().split())
    ids.append(s)
    dists.append(d)
    # Calcul du poids en multipliant v par 20
    weights.append(v * 20)

dic = {}  # Dictionnaire pour mémoriser les résultats intermédiaires (mémoïsation)
INF = 10 ** 20  # Constante représentant l'infini pour les comparaisons

def score(rest, pos, total_weight, order):
    """
    Calcule le score minimal et l'ordre correspondant pour visiter les points restants.

    Args:
        rest (int): Un masque binaire représentant les éléments restant à visiter.
        pos (int): L'indice de la position actuelle dans la liste.
        total_weight (int): Le poids total accumulé jusqu'à présent.
        order (list): La liste des indices dans l'ordre visité (non utilisée dans la récursion).
    
    Returns:
        tuple: Un tuple contenant :
            - float: Le score minimal calculé (coût total).
            - list: La liste des indices représentant l'ordre de visite optimisé.
    """
    # Cas de base : s'il n'y a plus d'éléments à visiter, le coût est nul
    if rest == 0:
        return 0, []
    # Retourner le résultat mémorisé si déjà calculé
    if (rest, pos) in dic:
        return dic[(rest, pos)]

    mask = 1
    # Initialiser le meilleur résultat avec l'infini et une liste vide
    ret = (INF, [])
    # Parcourir tous les éléments pour trouver le prochain à visiter
    for i in range(n):
        # Vérifier si l'élément i est encore à visiter dans le masque rest
        if rest & mask:
            # Calcul récursif du score pour le reste des éléments sans 'i'
            temp = score(rest & ~mask, i, total_weight + weights[i], order)
            # Calculer le coût en fonction de la distance, poids et appel récursif
            cost = temp[0] + abs(dists[pos] - dists[i]) / 2000 * (total_weight)
            # Comparer et choisir la solution minimale
            ret = min(ret, (cost, [i] + temp[1]))
        mask <<= 1  # Décaler le masque pour vérifier l'élément suivant
    
    # Mémoriser le résultat obtenu
    dic[(rest, pos)] = ret
    return ret

# Calcul du masque initial avec tous les éléments à visiter (tous les bits à 1)
rest = 2 ** n - 1
# Calcul du score minimal en testant chaque élément comme point de départ avec un poids initial de 70
result = min([score(rest, i, 70, []) for i in range(n)])
# Affichage de la liste des identifiants dans l'ordre optimal trouvé
print(*[ids[i] for i in result[1]])