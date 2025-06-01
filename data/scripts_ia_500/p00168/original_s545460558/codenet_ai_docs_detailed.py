from math import ceil

# Initialisation d'une liste 'dp' pour stocker le nombre de façons d'atteindre chaque position
# dp[i] représentera le nombre de façons d'arriver à la position i avec des pas de taille 1, 2 ou 3
dp = [1] + [0 for i in range(33)]  # dp[0] = 1 (une façon de rester au début), les autres sont initialisés à 0

# Calcul des façons d'atteindre chaque position de 0 à 33
for i in range(0, 30):
    # Pour chaque position, on ajoute les façons d'atteindre i+1, i+2 et i+3
    for step in [1, 2, 3]:
        dp[i + step] += dp[i]

unit = 3650.  # Unité de division pour le calcul final (float pour division précise)

def main():
    """
    Boucle principale qui lit des entrées utilisateur correspondant à des distances (n),
    puis affiche le nombre de jours nécessaires pour couvrir la distance,
    en arrondissant vers le haut après division par 'unit'.

    Le programme s'arrête lorsque l'utilisateur entre 0.
    """
    while True:
        # Lecture de la distance en entrée (en supposant une entrée valide)
        n = int(raw_input())

        # Condition d'arrêt si la distance est 0
        if n == 0:
            break

        # Calcul du nombre d'unités complètes nécessaires pour atteindre la distance n
        # dp[n] correspond au nombre de façons d'atteindre la position n
        # Le résultat est divisé par 'unit' puis arrondi vers le haut à l'entier supérieur
        result = int(ceil(dp[n] / unit))

        # Affichage du résultat final
        print result

# Exécution de la fonction principale
if __name__ == "__main__":
    main()