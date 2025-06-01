def moyenne_entiers():
    """
    Lit deux entiers depuis l'entrée standard, calcule leur moyenne arithmétique,
    puis affiche le résultat entier.

    Étapes :
    1. Lecture de deux entiers séparés par un espace via input().
    2. Conversion des entrées en entiers avec map.
    3. Calcul de la moyenne arithmétique.
    4. Conversion du résultat en entier (tronque la partie décimale).
    5. Affichage du résultat.
    """
    # Lecture et conversion des deux entiers saisis par l'utilisateur
    a, b = map(int, input("Entrez deux entiers séparés par un espace : ").split())

    # Calcul de la moyenne des deux entiers
    moyenne = (a + b) / 2

    # Conversion de la moyenne en entier pour supprimer la partie décimale
    moyenne_entiere = int(moyenne)

    # Affichage du résultat
    print(moyenne_entiere)

# Appel de la fonction pour exécuter le programme
moyenne_entiers()