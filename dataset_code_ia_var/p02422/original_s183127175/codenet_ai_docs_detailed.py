def my_print(s: str, args: list) -> str:
    """
    Extrait et retourne une sous-chaîne de la chaîne `s`.

    Args:
        s (str): La chaîne d'origine.
        args (list): Liste d'arguments, où args[0] est l'indice de début et args[1] l'indice de fin (tous deux inclus) 
                     pour l'extraction. Les deux doivent être convertibles en int.

    Returns:
        str: La sous-chaîne extraite de `s`, allant de l'indice start à l'indice end inclus.
    """
    # Conversion des indices en entiers
    start = int(args[0])
    end = int(args[1])
    # Extraction et renvoi de la sous-chaîne du début (start) à la fin (end) inclusivement
    return s[start: end + 1]

def my_reverse(s: str, args: list) -> str:
    """
    Inverse une portion de la chaîne `s` entre les indices spécifiés et retourne la nouvelle chaîne.

    Args:
        s (str): La chaîne d'origine.
        args (list): Liste d'arguments, où args[0] est l'indice de début et args[1] l'indice de fin (tous deux inclus) 
                     de la zone à inverser. Les deux doivent être convertibles en int.

    Returns:
        str: La chaîne `s` où la portion spécifiée a été inversée.
    """
    # Détermination des bornes à inverser
    start = int(args[0])
    end = int(args[1]) + 1  # +1 car la borne supérieure en slicing est exclue
    # Extraction de la portion à inverser
    to_reverse_string = s[start:end]
    # Reconstruction de la chaîne : début original + portion inversée + fin originale
    return s[:start] + to_reverse_string[::-1] + s[end:]

def my_replace(s: str, args: list) -> str:
    """
    Remplace une portion de la chaîne `s` par une nouvelle sous-chaîne.

    Args:
        s (str): La chaîne d'origine.
        args (list): Liste d'arguments, où args[0] est l'indice de début, args[1] l'indice de fin (tous deux inclus) 
                     de la zone à remplacer, et args[2] la chaîne de remplacement.

    Returns:
        str: La chaîne `s` où la portion spécifiée a été remplacée par `args[2]`.
    """
    # Conversion des indices en entiers
    start = int(args[0])
    end = int(args[1]) + 1  # +1 pour inclure l'indice de fin
    # Reconstruction de la chaîne : début original + chaîne de remplacement + fin originale
    return s[:start] + args[2] + s[end:]

def resolve():
    """
    Fonction principale qui lit la chaîne d'entrée, puis applique une série d'opérations ('print', 'reverse', 'replace') 
    selon les instructions lues. Les impressions sont faites dans le flux de sortie standard.
    """
    # Lecture de la chaîne d'origine
    s = input()
    # Lecture du nombre d'opérations à appliquer
    n = int(input())

    # Boucle sur chaque opération
    for _ in range(n):
        # Lecture et découpage de la commande : le nom de la fonction + ses arguments
        f, *args = input().split()

        # Si l'opération est 'print', afficher le résultat de la sous-chaîne extraite
        if f == 'print':
            print(my_print(s, args))
        # Si l'opération est 'reverse', inverser la portion spécifiée et mettre à jour la chaîne
        if f == 'reverse':
            s = my_reverse(s, args)
        # Si l'opération est 'replace', remplacer la portion spécifiée et mettre à jour la chaîne
        if f == 'replace':
            s = my_replace(s, args)

# Lancement du programme principal
resolve()