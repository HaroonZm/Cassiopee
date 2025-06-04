def replace_1_and_9(s):
    """
    Remplace tous les caractères '1' par '9' et tous les caractères '9' par '1' dans la chaîne d'entrée.
    Les autres caractères ne sont pas modifiés.

    Ce remplacement s’effectue en trois étapes pour éviter les conflits lors du remplacement direct :
      1. On remplace temporairement chaque '9' par un caractère de secours ('q'),
         afin de ne pas mélanger les remplacements de '1' et de '9'.
      2. On remplace alors tous les '1' par '9'.
      3. Enfin, on remplace tous les caractères de secours 'q' par '1'.
    
    Args:
        s (str): La chaîne de caractères d'entrée.

    Returns:
        str: La chaîne résultante avec les remplacements effectués.
    """
    # Remplacement temporaire de tous les '9' par le caractère de secours 'q'
    temp = s.replace('9', 'q')
    # Remplacement de tous les '1' par '9'
    temp = temp.replace('1', '9')
    # Remplacement final de tous les 'q' par '1'
    result = temp.replace('q', '1')
    return result

# Lecture de l'entrée utilisateur
s = input()

# Application de la fonction de remplacement et affichage du résultat
ans = replace_1_and_9(s)
print(ans)