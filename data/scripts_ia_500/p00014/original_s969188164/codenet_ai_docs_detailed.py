def calculate_sum():
    """
    Lit une série d'entiers depuis l'entrée standard et, pour chaque entier d, calcule une somme spécifique.

    Pour chaque entier d lu, la fonction effectue la somme S définie par :
    S = ∑_{i=0}^{(600//d)-1} ( (i*d)^2 * d )

    Cette somme est calculée en itérant i de 0 jusqu'à (600//d) exclus, où :
    - (i*d)^2 correspond à la variable 'tate'
    - d est la variable 'yoko'

    Le résultat est ensuite affiché sur une nouvelle ligne.

    La lecture s'arrête lorsque aucune donnée n'est disponible (détection d'EOF).
    """
    try:
        while True:
            # Lecture d'un entier depuis l'entrée standard
            d = int(input())

            # Initialisation de la somme à zéro pour ce calcul
            s = 0

            # Calcul du nombre d'itérations selon la division entière 600//d
            iterations = 600 // d

            # Boucle de calcul de la somme
            for i in range(iterations):
                # Calcul de la variable tate comme le carré de (i*d)
                tate = (i * d) ** 2

                # La variable yoko est égale à d
                yoko = d

                # Ajout du produit tate * yoko à la somme s
                s += tate * yoko

            # Affichage du résultat pour l'entier courant
            print(s)
    except EOFError:
        # Fin de la lecture des données, on sort proprement de la fonction
        pass


# Exécution de la fonction principale
calculate_sum()