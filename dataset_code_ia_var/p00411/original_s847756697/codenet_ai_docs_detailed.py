def calculate_expression(numbers):
    """
    Calcule l'expression (second élément / premier élément) * troisième élément à partir d'une liste de trois entiers.
    
    Args:
        numbers (list of int): Une liste contenant exactement trois entiers dans l'ordre [a, b, c].
    
    Returns:
        float: Le résultat du calcul (b / a) * c.
    """
    # Extraction des trois entiers pour une meilleure lisibilité
    a = numbers[0]
    b = numbers[1]
    c = numbers[2]
    # Calcul de l'expression demandée
    result = (b / a) * c
    return result

# Lecture d'une ligne depuis l'entrée utilisateur, séparée par des espaces
# La ligne est divisée en éléments, chacun converti en entier, puis stocké dans une liste
input_numbers = list(map(int, input().split()))

# Appel de la fonction pour calculer le résultat avec les nombres fournis en entrée
output = calculate_expression(input_numbers)

# Affichage du résultat à l'utilisateur
print(output)