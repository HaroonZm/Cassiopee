import math

def read_input():
    """
    Lit et analyse les données d'entrée de l'utilisateur.
    
    Returns:
        N (int): Nombre de personnes (hors soi-même) dans la pièce.
        C (int): Nombre de types de gâteaux.
        cakes (list of int): Liste du nombre de morceaux disponibles pour chaque type de gâteau.
    """
    # Lecture du nombre de personnes N et du nombre de types de gâteaux C
    N, C = list(map(int, input().split(' ')))
    # Lecture du nombre de morceaux pour chaque type de gâteau, sous forme de liste d'entiers
    cakes = list(map(int, input().split(' ')))
    return N, C, cakes

def calculate_my_cake(N, cakes):
    """
    Calcule le nombre de morceaux de gâteaux qu'une personne (vous) doit recevoir
    afin que la répartition soit équitable, en supposant qu'il y a N autres personnes.
    
    Args:
        N (int): Nombre de personnes (hors soi-même) dans la pièce.
        cakes (list of int): Liste du nombre de morceaux disponibles pour chaque type de gâteau.
        
    Returns:
        int: Nombre de morceaux de gâteau à recevoir (arrondi à l'entier supérieur).
    """
    # Calcul du nombre total de morceaux disponibles (tous types confondus)
    num_cakes = sum(cakes)
    # Nombre total de personnes à partager les gâteaux (N autres personnes + soi-même)
    total_people = N + 1
    # Calcul du nombre de morceaux par personne, arrondi vers le haut
    mycake = math.ceil(num_cakes / total_people)
    return mycake

def main():
    """
    Exécute le programme principal : lit les entrées, calcule la part de gâteau,
    puis affiche le résultat.
    """
    # Lecture des données d'entrée
    N, C, cakes = read_input()
    # Calcul du nombre de morceaux que l'utilisateur peut obtenir
    my_cake_share = calculate_my_cake(N, cakes)
    # Affichage du résultat
    print(my_cake_share)

# Appel du programme principal
main()