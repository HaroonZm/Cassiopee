def average_of_inputs():
    """
    Demande à l'utilisateur de saisir un nombre entier n, puis lit n entiers à partir de l'entrée standard.
    Calcule et affiche la moyenne entière des n entiers saisis.

    Entrée :
        - n (int) : le nombre d'entiers à saisir ensuite (doit être supérieur à 0).
        - Ensuite, n entiers chacun sur une ligne séparée.

    Sortie :
        - Affiche la moyenne entière (division entière) des n entiers.
    """
    # Demande à l'utilisateur le nombre d'entiers à saisir
    n = int(input("Entrez le nombre d'entiers à saisir : "))
    
    # Liste pour stocker les entiers saisis
    numbers = []
    
    # Utilise une boucle pour lire 'n' entiers à partir de l'entrée utilisateur
    for i in range(n):
        # Demande à l'utilisateur de saisir un entier
        number = int(input(f"Entrez l'entier numéro {i+1} : "))
        numbers.append(number)
    
    # Calcule la somme des entiers saisis
    total = sum(numbers)
    
    # Calcule la moyenne entière (division entière) des entiers saisis
    average = total // n
    
    # Affiche la moyenne entière
    print(average)

# Appel de la fonction principale pour exécuter le programme
average_of_inputs()