def update_population(r, d, x):
    """
    Met à jour la valeur de x pour 10 itérations selon la formule de récurrence :
    x_new = r * x - d à chaque itération, puis affiche la valeur obtenue.
    
    Args:
        r (int): Taux de croissance multiplicatif.
        d (int): Valeur soustraite à chaque itération (décroissance).
        x (int): Valeur initiale de la population ou du paramètre.
    """
    for i in range(10):
        # À chaque itération, on applique la relation de récurrence
        x = r * x - d
        # Affiche la valeur courante après mise à jour
        print(x)

if __name__ == "__main__":
    # Lit trois entiers de l'entrée standard correspondant à r, d, x
    r, d, x = map(int, input().split())
    # Lance la mise à jour et l'affichage des valeurs
    update_population(r, d, x)