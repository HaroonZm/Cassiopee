# AOJ 1011: Finding the Largest Carbon Compound
# Python3 2018.7.4 bal4u

def precompute_largest_compounds(max_index=31):
    """
    Pré-calcul des plus grands composés carbonés pour des indices de 1 à max_index.
    
    La formule de récurrence utilisée est:
    a[1] = 1
    a[2] = 2
    a[i] = 3 * a[i-2] + 2 pour i >= 3
    
    Args:
        max_index (int): L'indice maximal jusqu'où les valeurs sont calculées (par défaut 31).
        
    Returns:
        list: Une liste a où a[i] contient la valeur pré-calculée pour i.
    """
    a = [0] * (max_index + 1)
    a[1], a[2] = 1, 2
    for i in range(3, max_index + 1):
        a[i] = 3 * a[i - 2] + 2
    return a

def main():
    """
    Fonction principale qui lit des indices depuis l'entrée standard,
    puis affiche la plus grande valeur du composé carboné pré-calculée correspondant.
    
    La lecture se poursuit jusqu'à ce qu'une entrée invalide ou une fin de fichier soit rencontrée.
    """
    # Pré-calcul des valeurs jusqu'à l'indice 31
    a = precompute_largest_compounds(31)
    
    while True:
        try:
            # Lecture d'un entier depuis l'entrée standard
            i = int(input())
        except:
            # En cas d'erreur (fin de fichier ou entrée invalide), on quitte la boucle
            break
        # Affichage du résultat pré-calculé pour l'indice i
        print(a[i])

if __name__ == "__main__":
    main()