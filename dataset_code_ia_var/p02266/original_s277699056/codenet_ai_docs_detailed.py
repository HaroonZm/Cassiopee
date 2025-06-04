def calculate_water_pools(s):
    """
    Calcule la quantité totale d'eau accumulée entre des pentes représentées par des caractères,
    ainsi que la taille de chaque 'flaque'. Les pentes descendantes sont notées par '\',
    les ascendantes par '/', et les plateaux par '_', par exemple.
    
    Args:
        s (str): Une chaîne représentant une section transversale de terrain,
                 composée de '\', '/', et potentiellement d'autres caractères.
    
    Returns:
        tuple: Un tuple contenant :
          - La somme totale d'eau accumulée (int)
          - Une liste des tailles de chaque flaque (list of int)
    """
    a = []          # Liste pour stocker les paires [position de début, taille de la flaque]
    d = []          # Pile pour stocker les indices des barres descendantes '\'
    total = 0       # Variable pour la somme totale de l'eau accumulée

    for i, line in enumerate(s):
        if line == "\\":   # Début d'une nouvelle descente, ajoute l'indice dans la pile
            d.append(i)
        elif line == "/" and d: # Ascension : forme potentielle de flaque, traite si une descente correspondante existe
            j = d.pop()         # Récupère la position de la dernière descente
            size = i - j        # Calcul la taille de la flaque courante
            total += size       # Ajoute la taille à la somme totale

            # Fusionne les flaques intérieures lorsque la flaque courante les englobe
            while a and a[-1][0] > j:
                size += a.pop()[1]
            
            # Ajoute la flaque à la liste, avec son point de départ et sa taille
            a.append([j, size])

    # Extrait uniquement les tailles de flaques pour l'affichage ou l'utilisation ultérieure
    water_pools_sizes = [size for _, size in a]
    return total, water_pools_sizes

if __name__ == "__main__":
    # Lecture de l'entrée utilisateur
    s = input()

    # Calcul des flaques d'eau et leur somme totale
    total, water_pools_sizes = calculate_water_pools(s)

    # Affichage de la quantité totale d'eau accumulée
    print(total)

    # Affichage du nombre de flaques, puis de leur taille respective dans l'ordre
    print(len(water_pools_sizes), *water_pools_sizes)