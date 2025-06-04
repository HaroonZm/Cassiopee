def compute_change(a, b):
    """
    Calcule le nombre minimal de billets/pièces nécessaires pour rendre la monnaie
    entre deux montants. Le change est calculé pour les valeurs de 100, 500 et 1000.
    
    Paramètres:
        a (int): Le montant initial.
        b (int): Le montant final à atteindre ou à donner.
        
    Retourne:
        tuple: Nombre de pièces/billets de 100, 500 et 1000 respectivement.
    """
    # Calcul de la différence à rendre
    c = b - a

    # Calcul du nombre de billets de 1000 dans la différence
    t = c // 1000

    # Calcul du reste après retranchement des billets de 1000, puis du nombre de billets de 500
    f = (c - 1000 * t) // 500

    # Calcul du reste après retranchement des billets de 1000 et 500, puis du nombre de billets de 100
    h = (c - 1000 * t - 500 * f) // 100

    return h, f, t

def main():
    """
    Boucle principale qui lit les entrées utilisateur, calcule et affiche le changement à rendre.
    Le programme s'arrête lorsque l'utilisateur entre 0 comme première valeur.
    """
    while True:
        # Lecture de deux entiers séparés avec gestion de la compatibilité Python 2
        try:
            a, b = map(int, raw_input().split())
        except NameError:
            # Pour Python 3
            a, b = map(int, input().split())
        # Fin de la boucle si la première valeur entrée est 0
        if a == 0:
            break
        # Calcul du change à rendre avec la fonction dédiée
        h, f, t = compute_change(a, b)
        # Affichage du résultat
        print(h, f, t)

# Exécution du programme
if __name__ == '__main__':
    main()