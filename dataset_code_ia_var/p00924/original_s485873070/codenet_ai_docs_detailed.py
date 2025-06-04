import copy

# Lecture des entrées utilisateurs : N (nombre total d'éléments), M (nombre de blocs)
N, M = [int(i) for i in input().split()]

# Lecture de la configuration initiale sous forme de liste de bits
b = [int(i) for i in input().split()]

# Lecture de la taille de chaque bloc à permuter
p = [int(i) for i in input().split()]

def solve(num):
    """
    Calcule le nombre minimal d'échanges nécessaires pour organiser le tableau 'b'
    de sorte qu'il suive le motif alterné déterminé par 'num' (0 ou 1) en utilisant
    la structure de blocs de tailles 'p'.

    Args:
        num (int): Le motif de départ (0 ou 1) pour la structure cible.

    Returns:
        int: Le coût minimal (nombre de swaps nécessaires) ou 1000 si non réalisable.
    """
    ret = 0  # Nombre total de swaps effectués
    # Création d'une copie indépendante de 'b' pour ne pas modifier l'original
    c = copy.deepcopy(b)
    c_ = []  # Liste cible reconstituée selon le motif choisi
    
    # Construction du motif cible en concaténant chaque bloc
    # i%2==num détermine la valeur à placer dans chaque bloc selon l'alternance
    for i in range(M):
        c_ += [int(i % 2 == num)] * p[i]

    # Pour chaque position, tenter d'avoir la bonne valeur au bon endroit
    for i in range(N):
        if c[i] != c_[i]:
            # Recherche de la prochaine position où le motif cible correspond à la valeur actuelle
            for j in range(i, N):
                if c_[i] == c[j]:
                    # Inverse les deux éléments pour les mettre à la bonne place
                    ret += j - i  # Nombre de swaps nécessaires pour déplacer c[j] en position i
                    c[i], c[j] = c[j], c[i]
                    break
            else:
                # Si aucune correspondance n'est trouvée, il n'est pas possible de convertir
                return 1000
    return ret

# On teste avec les deux motifs de départ possibles (alternance débutant par 0 ou 1)
# et affiche la solution optimale
print(min(solve(0), solve(1)))