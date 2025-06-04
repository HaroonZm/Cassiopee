def add_two_numbers():
    """
    Lit deux valeurs numériques séparées par un espace depuis l'entrée standard,
    les convertit en entiers et affiche leur somme.

    Entrée :
        L'utilisateur doit saisir deux nombres séparés par un espace.
    Sortie :
        Affiche la somme des deux nombres saisis.
    """

    # Lire la ligne saisie par l'utilisateur
    user_input = input()

    # Séparer la ligne en deux parties (supposées être des nombres) à l'aide de split()
    a, b = user_input.split()

    # Convertir les deux parties en entiers
    int_a = int(a)
    int_b = int(b)

    # Additionner les deux entiers
    result = int_a + int_b

    # Afficher le résultat
    print(result)


# Lancer la fonction principale si ce script est exécuté directement
if __name__ == "__main__":
    add_two_numbers()