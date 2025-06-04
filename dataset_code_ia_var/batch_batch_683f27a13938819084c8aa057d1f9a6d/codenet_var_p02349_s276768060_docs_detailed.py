# Lecture du nombre de positions (N) et du nombre de requêtes (Q)
N, Q = map(int, input().split())

# Initialisation du tableau du Binary Indexed Tree (BIT/Fenwick tree)
# L'indice 0 n'est pas utilisé pour simplifier les opérations sur les indices (commence à 1)
data = [0] * (N + 1)

def add(k, x):
    """
    Ajoute la valeur x à la position k dans l'arbre de Fenwick (BIT).

    Args:
        k (int): L'indice de départ (1-based) où effectuer l'ajout.
        x (int): La valeur à ajouter.

    Cette fonction propage la valeur x sur tous les indices pertinents du BIT
    pour permettre une mise à jour efficace des plages.
    """
    while k <= N:
        data[k] += x
        k += k & -k  # Avance vers le prochain indice affecté dans le BIT

def get(k):
    """
    Calcule la somme préfixe des éléments jusqu'à l'indice k.

    Args:
        k (int): L'indice (1-based) jusqu'auquel on souhaite obtenir la somme.

    Returns:
        int: La somme de tous les ajouts inclusifs du BIT jusqu'à k.
    """
    s = 0
    while k:
        s += data[k]
        k -= k & -k  # Recule vers l'indice parent dans le BIT
    return s

ans = []  # Liste qui stockera les résultats des requêtes de type 1 (interrogation)

# Traitement des Q requêtes
for q in range(Q):
    a = input()
    if a[0] == "1":
        # Requête de type 1: interrogation de la valeur à une position donnée
        pos = int(a[2:])  # Extraction de l'indice à interroger (1-based)
        ans.append(str(get(pos)))
    else:
        # Requête de type 2: ajout d'une valeur x sur un segment [s, t]
        s, t, x = map(int, a[2:].split())
        add(s, x)  # Ajoute x à position s (début du segment)
        if t < N:
            add(t + 1, -x)  # Annule x à t+1 (fin du segment + 1) si dans les bornes

# Affichage de toutes les réponses aux requêtes de type 1
for i in ans:
    print(i)