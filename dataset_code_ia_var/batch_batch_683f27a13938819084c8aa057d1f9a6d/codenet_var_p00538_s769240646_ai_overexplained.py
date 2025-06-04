import sys  # Importe le module système, qui fournit des fonctionnalités spécifiques au système d'exploitation, comme la gestion de la récursivité

sys.setrecursionlimit(100000)  # Augmente la limite par défaut de la profondeur de récursion pour permettre des appels récursifs profonds (ici à 100 000)

# Lit toutes les entrées depuis l'entrée standard (par exemple, le terminal ou un fichier par redirection)
# split() découpe la chaîne en une liste de chaînes, séparées par des espaces ou des retours à la ligne
# map(int, ...) convertit chaque élément en entier
# Le premier entier lu est N (le nombre d'éléments), les suivants sont stockés dans la liste A
N, *A = map(int, open(0).read().split())

# Crée une table de mémoïsation pour stocker les résultats intermédiaires et éviter de refaire des calculs inutilement
# Il s'agit d'une liste de N listes, chacune contenant N éléments initialisés à -1 (ce qui signifie 'pas encore calculé')
memo = [[-1] * N for i in range(N)]  # 'for i in range(N)' itère N fois pour créer N sous-listes

# Initialise la diagonale principale de la table de mémoïsation
# Ceci correspond à la situation où la séquence ne contient qu'un seul élément (p == q)
# Si le nombre d'éléments N est impair (N % 2 == 1), le joueur courant peut prendre l'élément
# Sinon, si N est pair, la valeur est mise à 0 (le joueur courant ne peut rien gagner)
for i in range(N):  # Boucle pour chaque position de la séquence circulaire
    if N % 2:  # Si N est impair
        memo[i][i] = A[i]  # Le seul élément disponible est pris, c'est la valeur de A[i]
    else:  # Si N est pair
        memo[i][i] = 0  # Il n'y a rien à gagner dans ce cas précis

# Définit une fonction de recherche récursive 'dfs' (depth-first search) pour calculer la valeur maximale possible
# p : index de début, q : index de fin, t : variable pour indiquer le joueur courant (1 pour le joueur principal, 0 pour l'adversaire)
def dfs(p, q, t):
    # Vérifie si la valeur pour ce sous-problème a déjà été calculée
    if memo[p][q] != -1:  # Si ce cas a déjà été traité
        return memo[p][q]  # Retourne la valeur mémorisée, évite de recalculer

    # Si t est vrai (c'est au tour du joueur principal de jouer)
    if t:
        # Deux options s'offrent au joueur principal :
        # 1. Prendre l'élément à la position 'p', puis c'est au tour de l'adversaire de jouer sur la sous-séquence [p+1, q]
        # 2. Prendre l'élément à la position 'q', puis c'est au tour de l'adversaire de jouer sur la sous-séquence [p, q-1]
        # %N permet de gérer l'aspect circulaire de la séquence (pour que les indices restent dans les bornes)
        val1 = A[p] + dfs((p+1)%N, q, 0)  # Option 1
        val2 = A[q] + dfs(p, (q-1)%N, 0)  # Option 2
        r = max(val1, val2)  # Le joueur principal choisit le maximum des deux options
        memo[p][q] = r  # Mémorise le résultat pour ce sous-problème
    else:
        # Au tour de l'adversaire : il va choisir la solution qui minimise le score du joueur principal à son prochain tour
        # C'est-à-dire, il enlève le plus grand ou le plus petit selon la configuration
        if A[p] < A[q]:
            # Si la valeur à la position 'p' est inférieure à celle à la position 'q', l'adversaire va retirer celle qui gêne le plus (ici 'p')
            r = dfs(p, (q-1)%N, 1)  # L'adversaire enlève 'q', on continue sur [p, q-1]
        else:
            # Sinon, l'adversaire enlève 'p', on continue sur [p+1, q]
            r = dfs((p+1)%N, q, 1)
        memo[p][q] = r  # Mémorise le résultat pour ce sous-problème

    # Retourne la valeur calculée ou mémorisée pour ce sous-problème
    return r

# Calcule la réponse maximale en testant tous les choix de départ possible (c'est un jeu circulaire donc il faut tester tous les 'i')
ans = 0  # Initialise la meilleure réponse trouvée à 0 (pire cas)
for i in range(N):  # Pour chaque position possible de départ
    # Laisse le joueur principal commencer à la position 'i'
    # dfs((i+1)%N, (i-1)%N, 0) : Le reste de la séquence après avoir choisi 'i', en passant le tour à l'adversaire (t = 0)
    score = A[i] + dfs((i+1)%N, (i-1)%N, 0)  # Le joueur principal ajoute la valeur de A[i] au meilleur score qu'il peut obtenir ensuite
    ans = max(ans, score)  # Met à jour la meilleure réponse trouvée

# Affiche le résultat final (la valeur maximale possible pour le joueur principal, quelle que soit la position de départ)
print(ans)  # Affiche la réponse sur la sortie standard (console)