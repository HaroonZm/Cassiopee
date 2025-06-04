import sys  # Importe le module sys, utilisé pour interagir avec l'entrée et la sortie standard

# Assigner la fonction readline (pour lire une ligne de l'entrée standard) à la variable readline
readline = sys.stdin.readline

# Lire une ligne, la découper selon les espaces et convertir chaque morceau en entier
# Cela donne deux entiers : N (taille du tableau), K (nombre d'opérations à effectuer)
N, K = map(int, readline().split())

# Lire la ligne suivante, découper selon les espaces et convertir chaque morceau en entier
# On ajoute un 0 en début de liste pour que la liste soit 1-indicée, c'est-à-dire que l'index 1 de la liste corresponde au premier élément logique, facilitant l'accès dans un contexte où les indices commencent à 1
A = [0] + list(map(int, readline().split()))

# On initialise la variable now à 1
# Cette variable représente la 'position actuelle' dans la chaîne de sauts (à partir de l'index 1)
now = 1

# Boucle principale : on continue tant que K n'est pas nul
while K:
    # Si le bit de poids faible de K est à 1 (opération AND entre K et 1)
    # Cela signifie que pour ce bit de K, il faut faire un saut depuis la position now
    if K & 1:
        # Mettre à jour now en sautant vers la position indiquée par A[now]
        now = A[now]

    # Créer un nouveau tableau nex de taille N+1, initialisé avec des zéros
    # Ce tableau servira à calculer les 'doubles sauts' : nex[i] sera le résultat de deux sauts consécutifs
    nex = [0] * (N + 1)
    
    # Boucler sur toutes les positions possibles (de 0 à N inclus)
    for i in range(N + 1):
        # Pour chaque i, on définit nex[i] comme étant la position atteinte après deux sauts depuis i
        # Cela revient à appliquer la fonction A deux fois : d'abord A[i], puis A[A[i]]
        nex[i] = A[A[i]]
    
    # Mettre à jour le tableau A pour qu'il devienne la table des doubles sauts
    # Cela correspond à la montée binaire, utile pour traiter rapidement les grands K
    A = nex

    # Décaler K d'un bit vers la droite (division entière par 2)
    # Cela permet de traiter le bit suivant lors de la prochaine itération
    K >>= 1

# À la fin de toutes les opérations, afficher la position actuelle
print(now)