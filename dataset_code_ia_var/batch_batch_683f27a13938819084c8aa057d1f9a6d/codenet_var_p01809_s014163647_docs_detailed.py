def gcd(a, b):
    """
    Calcule le plus grand commun diviseur (PGCD) de deux nombres entiers a et b
    en utilisant l'algorithme d'Euclide.

    Args:
        a (int): Premier entier.
        b (int): Deuxième entier.

    Returns:
        int: Le PGCD de a et b.
    """
    while b:
        a, b = b, a % b
    return a

def main():
    """
    Lit deux entiers depuis l'entrée standard, calcule la partie de droite réduite par leur PGCD,
    puis trouve et affiche le produit de tous les facteurs premiers distincts de cette partie et le reste.
    
    Si le nombre final n'est pas 1, alors il y a un facteur premier restant qui doit être inclus;
    sinon, tous les facteurs premiers ont déjà été pris en compte.
    """
    # Lecture de deux entiers séparés par un espace
    a, b = map(int, input().split())

    # Réduction de b par le PGCD de a et b
    g = gcd(a, b)
    b //= g

    # Initialisation pour la recherche des facteurs premiers
    facteur = 2
    produit_facteurs_distincts = 1

    # Parcours de tous les candidats facteurs premiers jusqu'à racine carrée de b
    while facteur * facteur <= b:
        # Si le nombre courant divise b, c'est un facteur premier
        if b % facteur == 0:
            produit_facteurs_distincts *= facteur  # On multiplie le produit par ce facteur premier

            # Elimine toutes les occurrences de ce facteur
            while b % facteur == 0:
                b //= facteur
        facteur += 1  # On passe au facteur suivant

    # Après la boucle, s'il reste un facteur premier plus grand que racine carrée de b
    # alors il faut le prendre en compte
    if b != 1:
        # Si b n'est pas 1, alors c'est le dernier facteur premier
        print(produit_facteurs_distincts * b)
    else:
        print(produit_facteurs_distincts)

if __name__ == "__main__":
    main()