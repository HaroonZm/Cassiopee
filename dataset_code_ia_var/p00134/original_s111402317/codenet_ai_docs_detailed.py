def calculate_average_from_inputs():
    """
    Lit un entier `n` depuis l'entrée standard, puis lit `n` entiers supplémentaires.
    Calcule et retourne la moyenne entière (division entière) des `n` entiers saisis.

    Retours:
        int: La moyenne entière des entiers fournis en entrée.
    """
    # Lecture du nombre d'entiers à saisir
    n = int(input("Veuillez entrer le nombre de valeurs à saisir : "))
    
    # Initialisation d'une liste vide pour stocker les entiers saisis
    numbers = []
    
    # Boucle pour lire 'n' entiers, un à un, depuis l'entrée standard
    for i in range(n):
        value = int(input(f"Entrez l'entier numéro {i+1} : "))
        numbers.append(value)
    
    # Calcul de la somme de tous les entiers saisis
    total = sum(numbers)
    
    # Calcul de la moyenne entière (division entière)
    average = total // n
    
    # Retourne la valeur calculée
    return average

# Appel de la fonction et affichage du résultat
print(calculate_average_from_inputs())