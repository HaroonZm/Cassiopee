def average_input_numbers():
    """
    Lit un nombre n depuis l'entrée standard, puis lit n nombres entiers depuis l'entrée utilisateur,
    calcule et affiche la moyenne entière de ces nombres.
    """
    # Lecture de la valeur n (nombre de valeurs à lire ensuite) sous forme de chaîne de caractères.
    n = input()
    # Conversion de n en entier pour l'utiliser comme nombre d'itérations.
    n = int(n)
    
    # Création d'une liste des n nombres entiers lus via raw_input().
    # On utilise une list comprehension pour construire rapidement la liste.
    numbers = []
    for i in range(n):
        # Lecture d'une valeur de l'utilisateur (saisie clavier)
        value = raw_input()
        # Conversion de la valeur en entier avant de l'ajouter à la liste.
        value_int = int(value)
        numbers.append(value_int)
    
    # Calcul de la somme des n entiers.
    total = sum(numbers)
    # Calcul de la moyenne entière (division entière).
    average = total // n
    # Affichage de la moyenne.
    print(average)

# Appel de la fonction principale.
average_input_numbers()