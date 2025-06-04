def find_original_price(after_tax_price):
    """
    Trouve et retourne le prix avant taxe qui, après application d'une TVA de 8%, donne le prix arrondi (floor) égal à after_tax_price.

    Args:
        after_tax_price (int): Prix après application de la TVA (entrée utilisateur).

    Returns:
        int or None: Le prix original avant taxe si trouvé, sinon None.
    """
    import math

    # Parcours de tous les entiers possibles pour le prix initial (avant taxe)
    for i in range(1, 46298):
        # Calcul du prix après ajout de 8% de taxe, arrondi à l'entier inférieur
        if math.floor(i * 1.08) == after_tax_price:
            # Retourne le prix initial si la condition est satisfaite
            return i
    # Retourne None si aucun prix initial ne convient
    return None

def main():
    """
    Fonction principale qui gère l'entrée utilisateur, la recherche du prix initial et l'affichage du résultat.
    """
    # Lecture d'un entier depuis l'entrée standard (l'utilisateur doit entrer le prix après taxe)
    n = int(input())

    # Appel de la fonction pour trouver le prix original
    original_price = find_original_price(n)

    if original_price is not None:
        # Si un prix original (avant taxe) a été trouvé, l'afficher
        print(original_price)
    else:
        # Sinon, afficher ":(" pour indiquer qu'aucun prix ne convient
        print(":(")

if __name__ == "__main__":
    main()