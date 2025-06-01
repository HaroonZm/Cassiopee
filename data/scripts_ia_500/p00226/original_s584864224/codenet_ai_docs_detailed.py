def count_matching_positions(str1, str2):
    """
    Compte le nombre de positions où deux chaînes de caractères ont le même caractère.

    Args:
        str1 (str): La première chaîne de caractères.
        str2 (str): La deuxième chaîne de caractères.

    Returns:
        int: Le nombre de positions où les caractères de str1 et str2 correspondent.
    """
    count = 0
    for i in range(4):
        if str1[i] == str2[i]:
            count += 1
    return count

def count_common_characters(str1, str2):
    """
    Compte le nombre total de caractères dans str1 qui apparaissent dans str2, sans tenir compte des positions.
    
    Args:
        str1 (str): La première chaîne de caractères.
        str2 (str): La deuxième chaîne de caractères.
        
    Returns:
        int: Le nombre de caractères de str1 présents dans str2.
    """
    count = 0
    for char in str1:
        if char in str2:
            count += 1
    return count

def main():
    """
    Programme principal qui lit des paires de chaînes de caractères de longueur 4, puis affiche pour chaque paire :
    - Le nombre de positions où les caractères sont identiques.
    - Le nombre de caractères communs mais à des positions différentes.

    La lecture s'arrête lorsque les deux chaînes sont "0".

    Entrée:
        Paires de chaînes séparées par un espace, par ligne.

    Sortie:
        Pour chaque paire lue (sauf "0 0"), affiche deux nombres sur la même ligne séparés par un espace.
    """
    while True:
        a, b = input().split()
        # Condition d'arrêt : les deux chaînes sont "0"
        if a == b == "0":
            break
        
        # Compter les caractères identiques à la même position
        count = count_matching_positions(a, b)
        print(count, end=" ")
        
        # Compter tous les caractères communs
        newcount = count_common_characters(a, b)
        # Affiche le nombre de caractères communs mais pas à la même position
        print(newcount - count)

if __name__ == "__main__":
    main()