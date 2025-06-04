def calculate_rounded_amount(years):
    """
    Calcule et affiche le montant d'un capital de départ soumis à des intérêts composés annuels,
    en arrondissant à chaque itération le montant à l'entier de mille supérieur si nécessaire.
    
    Args:
        years (int): Nombre d'années pendant lesquelles le capital est placé.
        
    Returns:
        int: Le capital final après avoir appliqué les intérêts et les arrondis successifs.
    """
    # Montant de départ du capital
    a = 100000

    # Parcours chaque année (itération)
    for i in range(years):
        # Application d'une augmentation de 5% sur le montant actuel
        a *= 1.05

        # Vérification si le montant est déjà un multiple de 1000
        if a % 1000 == 0:
            # Si oui, aucune modification nécessaire (on passe)
            pass
        else:
            # Sinon, on arrondit à l'entier de mille supérieur
            a = (a + 1000) - a % 1000

    # Conversion du montant final en entier pour l'affichage/la sortie
    return int(a)

def main():
    """
    Point d'entrée principal du programme.
    Demande à l'utilisateur d'entrer le nombre d'années, puis affiche le capital final après calcul.
    """
    # Demande à l'utilisateur de saisir le nombre d'années (doit être un entier)
    years = int(input())

    # Appel de la fonction de calcul avec le nombre d'années donné et affichage du résultat
    print(calculate_rounded_amount(years))

if __name__ == "__main__":
    main()