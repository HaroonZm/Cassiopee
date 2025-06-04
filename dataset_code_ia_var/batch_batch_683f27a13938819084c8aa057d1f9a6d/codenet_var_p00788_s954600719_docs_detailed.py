import math

def find_closest_fractions(p, n):
    """
    Trouve les fractions irréductibles ayant un dénominateur au plus égal à n, 
    dont le quotient est entourant la racine carrée de p (plus proches fractionnellement en-dessous et au-dessus).
    
    Args:
        p (int): Le nombre dont on considère la racine carrée.
        n (int): Limite supérieure du dénominateur des fractions recherchées.
    
    Returns:
        tuple: (num_larger, denom_larger, num_smaller, denom_smaller)
               La première fraction est la plus grande en-dessous de sqrt(p),
               la seconde la plus petite au-dessus.
    """
    sqrt_p = math.sqrt(p)
    
    # Initialisation :
    # 'smaller' = [valeur_quotion, numérateur, dénominateur] pour la fraction en dessous de sqrt(p)
    # 'larger' = [valeur_quotion, numérateur, dénominateur] pour la fraction au dessus de sqrt(p)
    smaller = [
        math.floor(sqrt_p),        # Valeur initiale du quotient
        int(math.floor(sqrt_p)),   # Numérateur initial (entier inférieur)
        1                          # Dénominateur initial
    ]
    larger = [
        math.ceil(sqrt_p),         # Valeur initiale du quotient
        int(math.ceil(sqrt_p)),    # Numérateur initial (entier supérieur)
        1                          # Dénominateur initial
    ]
    
    # On parcours tous les numérateurs pertinents pour trouver les meilleures fractions
    for numerator in range(int(math.floor(sqrt_p)) + 1, n + 1):
        # Calcul du plus petit dénominateur qui garde le quotient inférieur à sqrt_p
        denom_smaller = math.ceil(numerator / sqrt_p)
        # Calcul du plus grand dénominateur qui garde le quotient supérieur à sqrt_p
        denom_larger = math.floor(numerator / sqrt_p)
        
        # Mise à jour de la meilleure fraction en-dessous de sqrt_p
        if numerator / denom_smaller > smaller[0]:
            # Vérifie si la fraction n'est pas alignée avec le point initial pour éviter les doublons
            if (smaller[1] * denom_smaller) / float(smaller[2]) != numerator:
                smaller = [numerator / denom_smaller, numerator, int(denom_smaller)]
        
        # Mise à jour de la meilleure fraction au-dessus de sqrt_p
        if numerator / denom_larger < larger[0]:
            if (larger[1] * denom_larger) / float(larger[2]) != numerator:
                larger = [numerator / denom_larger, numerator, int(denom_larger)]
    
    return (larger[1], larger[2], smaller[1], smaller[2])


def main():
    """
    Fonction principale qui lit l'entrée utilisateur,
    traite chaque paire (p, n) et affiche les résultats.
    Sort de la boucle lorsque p vaut 0.
    """
    while True:
        # Lecture et parsing de la ligne d'entrée
        p_n_input = raw_input()
        p, n = [int(x) for x in p_n_input.split()]
        
        # Condition d'arrêt du programme
        if p == 0:
            break
        
        # Recherche des fractions intéressantes
        num_larger, denom_larger, num_smaller, denom_smaller = find_closest_fractions(p, n)
        
        # Affichage au format demandé
        print(str(num_larger) + "/" + str(denom_larger) + " " + str(num_smaller) + "/" + str(denom_smaller))


if __name__ == '__main__':
    main()