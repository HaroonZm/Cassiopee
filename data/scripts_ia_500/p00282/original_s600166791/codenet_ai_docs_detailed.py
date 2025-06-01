import math

def split_number_into_chunks(num, chunk_sizes):
    """
    Divise un nombre entier en plusieurs segments définis par les puissances de 10 fournies.

    Args:
        num (int): Le nombre entier à diviser.
        chunk_sizes (list of int): Liste des exposants pour les puissances de 10, 
                                   chaque élément représente la taille d'un segment.

    Returns:
        list of int: Liste des segments extraits du nombre, du plus grand au plus petit.
    """
    chunks = []
    remaining = num
    for exponent in chunk_sizes:
        # Calculer la puissance de 10 correspondante à la taille du segment
        divisor = pow(10, exponent)
        # Extraire la partie correspondante au segment
        chunk = remaining // divisor
        chunks.append(chunk)
        # Mettre à jour le reste pour les prochaines extractions
        remaining = remaining % divisor
    # Ajouter la dernière partie restante comme le dernier segment
    chunks.append(remaining)
    return chunks

def format_number_with_units(chunks, units):
    """
    Formate une liste de segments numériques en une chaîne de caractères avec des unités associées,
    en omettant les segments nuls.

    Args:
        chunks (list of int): Liste de segments numériques.
        units (list of str): Liste de chaînes représentant les unités correspondant à chaque segment.

    Returns:
        str: Chaîne formatée combinant les segments non nuls avec leurs unités respectives.
    """
    result = ''
    for value, unit in zip(chunks, units):
        if value != 0:
            # Concaténer la valeur et l'unité
            result += str(value) + unit
    return result

def main():
    """
    Fonction principale qui lit des paires d'entiers m, n depuis l'entrée standard,
    calcule m^n, divise le résultat en segments selon des puissances de 10 spécifiques,
    puis affiche le résultat formaté avec des unités personnalisées. L'exécution s'arrête
    lorsque la paire (0, 0) est lue.
    """
    # Définition des puissances de 10 utilisées pour segmenter le nombre
    # Ces exposants sont dans l'ordre décroissant correspondant à la segmentation du nombre
    chunk_sizes = [68, 64, 60, 56, 52, 48, 44, 40, 36, 32, 28, 24, 20, 16, 12, 8, 4]
    
    # Liste des unités associées à chaque segment (le dernier segment n'a pas d'unité)
    units = [
        'Mts','Fks','Nyt','Asg','Ggs','Gok','Sai','Sei',
        'Kan','Ko','Jou','Jo','Gai','Kei','Cho','Oku','Man',''
    ]
    
    while True:
        # Lecture de deux entiers séparés par un espace
        m, n = map(int, input().split())
        
        # Condition d'arrêt si les deux entiers sont nuls
        if m == 0 and n == 0:
            break
        
        # Calcul de la puissance m^n
        num = pow(m, n)
        
        # Diviser le nombre en segments selon les tailles définies
        chunks = split_number_into_chunks(num, chunk_sizes)
        
        # Formater et afficher le résultat en combinant les segments avec les unités
        formatted_result = format_number_with_units(chunks, units)
        print(formatted_result)

# Exécution du programme principal
if __name__ == "__main__":
    main()