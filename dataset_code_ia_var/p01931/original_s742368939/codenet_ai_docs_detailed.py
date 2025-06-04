def find_first_double_x(length, sequence):
    """
    Trouve la première position où deux 'x' consécutifs apparaissent dans la séquence.
    
    Args:
        length (int): Longueur de la séquence.
        sequence (str): Chaîne de caractères à analyser.
    
    Returns:
        int: La position (1-indexée) juste après l'apparition du premier double 'x'.
             Si aucun double 'x' n'est trouvé, retourne la longueur originale.
    """
    # Parcourir la séquence jusqu'à l'avant-dernier caractère
    for i in range(length - 1):
        # Vérifier si le caractère actuel et le suivant sont tous les deux 'x'
        if sequence[i] == 'x' and sequence[i + 1] == 'x':
            # Retourner la position 1-indexée du deuxième 'x'
            return i + 1
    # Si aucun double 'x' n'a été trouvé, retourner la valeur initiale de length
    return length


if __name__ == "__main__":
    # Lire la longueur de la chaîne à partir de l'entrée standard
    n = int(input())
    # Lire la chaîne de caractères à vérifier
    s = input()
    # Appeler la fonction et afficher le résultat
    result = find_first_double_x(n, s)
    print(result)