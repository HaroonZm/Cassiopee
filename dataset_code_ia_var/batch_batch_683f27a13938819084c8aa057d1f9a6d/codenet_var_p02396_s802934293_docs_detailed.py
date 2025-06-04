def main():
    """
    Fonction principale qui lit un entier depuis l'entrée standard et,
    tant que l'entier est compris entre 1 et 10000 inclus, affiche la valeur saisie
    en l'associant à un numéro de "case" correspondant à l'ordre d'entrée.
    L'entrée d'une valeur hors du domaine 1-10000 termine la boucle.
    """
    # Lecture initiale de la première valeur
    x = int(input())
    for i in range(10000):
        # Vérification que x est dans l'intervalle autorisé
        if x in range(1, 10001):
            n = i + 1  # Calcul du numéro de case (l'indice commence à 1)
            # Affichage formaté de la valeur actuelle avec le numéro de case
            print("Case " + str(n) + ": " + str(x))
            # Lecture de la valeur suivante pour la boucle
            x = int(input())

if __name__ == "__main__":
    main()