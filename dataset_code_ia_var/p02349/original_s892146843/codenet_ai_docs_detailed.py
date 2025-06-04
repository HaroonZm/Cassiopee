import sys

# Lecture optimisée de l'entrée
readline = sys.stdin.readline
# Ecriture optimisée de la sortie
write = sys.stdout.write

# Lecture des deux premiers entiers : taille du tableau (N) et nombre de requêtes (Q)
N, Q = map(int, readline().split())

# Initialisation de la structure de données pour gérer les opérations de plage (BIT/Fenwick Tree)
# L'indexation commence à 1 pour faciliter la gestion avec l'arbre de Fenwick
data = [0] * (N + 1)

def add(k, x):
    """
    Effectue une addition de 'x' à la position 'k' dans l'arbre de Fenwick.

    Cette opération met à jour les éléments nécessaires pour que l'arbre de Fenwick
    maintienne correctement les sommes préfixes pour les requêtes ultérieures.

    Args:
        k (int): L'indice 1-based à modifier.
        x (int): La valeur à ajouter à l'indice 'k'.
    """
    while k <= N:
        data[k] += x
        k += k & -k  # Passe à l'indice suivant selon la structure Fenwick

def get(k):
    """
    Calcule la somme des valeurs dans la plage 1..k (inclus) à l'aide de l'arbre de Fenwick.

    Args:
        k (int): L'indice 1-based jusqu'où cumuler la somme.

    Returns:
        int: La somme de la plage [1, k] dans le tableau.
    """
    s = 0
    while k:
        s += data[k]
        k -= k & -k  # Remonte vers les parents dans l'arbre de Fenwick
    return s

# Liste pour stocker les résultats des requêtes de type 'get'
ans = []

# Lecture et traitement de chacune des Q requêtes
for _ in range(Q):
    # Lecture d'une ligne, décodage du type et des paramètres de la requête
    line = readline().split()
    t, *cmd = map(int, line)
    if t:
        # t == 1 : requête de somme d'un point, cmd[0] = position
        ans.append(str(get(cmd[0])))
    else:
        # t == 0 : requête de mise à jour de plage [s, t] d'un incrément x
        s, t_idx, x = cmd
        add(s, x)  # Ajoute x à data[s]
        if t_idx < N:
            add(t_idx + 1, -x)  # Retranche x à data[t+1] (si dans le tableau) pour bornage de la plage

# Écriture optimisée de tous les résultats de requêtes de type 'get'
write("\n".join(ans))
write("\n")