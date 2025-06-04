def main():
    """
    Point d'entrée principal du programme.
    Lit la taille de la liste, puis la liste de hauteurs, et calcule
    le coût minimum pour atteindre la dernière position en respectant
    certaines règles de déplacement. Affiche le coût total minimal.

    Algorithme :
    - Remplit le tableau des coûts c[] de manière dynamique.
    - À chaque position, choisit le chemin minimal : depuis la position précédente
      ou celle d'avant selon la règle.
    """
    # Lit la taille de la séquence
    N = int(input())
    # Lit les hauteurs sous forme de liste d'entiers
    h = [int(i) for i in input().split()]
    # Initialise le tableau des coûts avec des zéros
    c = [0] * N

    # Coût d'accès à la première position est toujours 0 (position initiale)
    c[0] = 0
    # Coût pour atteindre la deuxième position (différence absolue entre les deux premières valeurs)
    c[1] = abs(h[1] - h[0])

    # Calcul du coût minimum pour chaque position à partir de la troisième
    for i in range(2, N):
        # On peut venir de l'élément précédent ou celui d'avant encore (i-1 ou i-2)
        # On choisit la solution la moins coûteuse parmi les deux
        saut_simple = abs(h[i] - h[i-1]) + c[i-1]
        saut_double = abs(h[i] - h[i-2]) + c[i-2]
        c[i] = min(saut_simple, saut_double)

    # Affichage du coût minimum total pour arriver à la dernière position
    print(c[N-1])