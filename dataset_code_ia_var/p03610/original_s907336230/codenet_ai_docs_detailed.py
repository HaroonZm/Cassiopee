def print_even_index_chars():
    """
    Demande à l'utilisateur de saisir une chaîne de caractères, puis
    affiche les caractères se trouvant à des indices pairs (0, 2, 4, ...).

    La fonction utilise la syntaxe de tranchage (slicing) de Python
    pour sélectionner les caractères désirés.
    """
    # Demander à l'utilisateur d'entrer une chaîne de caractères via l'entrée standard
    s = input("Veuillez entrer une chaîne de caractères : ")
    # Afficher les caractères aux indices pairs en utilisant le slicing [::2]
    # Ceci sélectionne tous les caractères de la chaîne s, en sautant un caractère à chaque fois
    print(s[::2])

# Appel de la fonction principale pour exécuter le programme
print_even_index_chars()