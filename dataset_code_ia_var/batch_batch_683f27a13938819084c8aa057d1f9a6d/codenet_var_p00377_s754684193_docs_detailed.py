def calculate_cake_share(num_people, num_cakes, cake_pieces):
    """
    Calcule la part de gâteau à attribuer à chaque personne en fonction du nombre
    de personnes, du nombre de gâteaux, et de la liste des parts de chaque gâteau.

    Args:
        num_people (int): Le nombre de personnes à partager le gâteau (hors soi-même).
        num_cakes (int): Le nombre de gâteaux.
        cake_pieces (list of int): Une liste contenant le nombre de parts dans chaque gâteau.

    Returns:
        int: La part de gâteau (arrondie au supérieur si nécessaire) à attribuer à chacun.
    """
    # Calcul du nombre total de parts disponibles en sommant toutes les parts des gâteaux
    total_pieces = sum(cake_pieces)
    
    # On divise le nombre total de parts par le nombre de personnes plus soi-même
    # L'arrondi au supérieur se fait en ajoutant 1 si le reste est supérieur à 0
    share = total_pieces // (num_people + 1)
    if total_pieces % (num_people + 1) > 0:
        share += 1
    return share

if __name__ == "__main__":
    # Lecture des entrées utilisateur pour le nombre de personnes et de gâteaux
    n, c = list(map(int, input().split()))
    
    # Lecture de la liste de parts pour chaque gâteau
    pli = list(map(int, input().split()))

    # Appel de la fonction pour calculer la part de gâteau à attribuer
    mycake = calculate_cake_share(n, c, pli)
    
    # Affichage du résultat
    print(mycake)