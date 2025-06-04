def main():
    """
    Fonction principale exécutant une boucle infinie pour traiter plusieurs jeux de données,
    puis terminant lorsque l'entrée correspond à (0, 0, 0).
    Pour chaque jeu de données :
        - 'n' est le nombre d'éléments
        - 'm' est l'indice (1-based) de l'élément spécifique à traiter
        - 'p' est un pourcentage (exprimé comme un entier)
    La fonction lit 'n' entiers supplémentaires et calcule un résultat basé sur les entrées.
    """

    while True:
        # Lire trois entiers qui représentent respectivement :
        # n : nombre total d'éléments
        # m : l'indice de l'élément de référence (1-based)
        # p : un pourcentage à appliquer
        n, m, p = map(int, input().split())

        # Condition d'arrêt : si les trois valeurs sont nulles, sortir de la boucle
        if (n, m, p) == (0, 0, 0):
            break

        # Lire 'n' entiers depuis l'entrée standard et les stocker dans la liste x
        x = [int(input()) for _ in range(n)]

        # Si l'élément d'indice m-1 est zéro, le résultat est automatiquement 0
        if x[m-1] == 0:
            print(0)
        else:
            # Sinon, calculer la somme totale, multiplier par (100 - p),
            # puis diviser par x[m-1] pour obtenir le résultat demandé.
            # Le résultat est ensuite converti en entier (arrondi vers zéro)
            total_points = sum(x)
            adjusted_total = total_points * (100 - p)
            result = int(adjusted_total / x[m-1])
            print(result)

if __name__ == "__main__":
    main()