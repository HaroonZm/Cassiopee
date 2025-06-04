def calculate_special_sum():
    """
    Lit un entier N et une liste de N entiers depuis l'entrée standard.
    Calcule une somme spéciale comme suit :
      - Si le produit de tous les éléments est positif ou nul, affiche la somme de leurs valeurs absolues.
      - Si le produit est négatif, affiche la somme des valeurs absolues diminuée de deux fois la plus petite valeur absolue.
    """
    # Lecture du nombre d'éléments à traiter
    N = int(input())
    
    # Lecture de la liste des entiers depuis l'entrée standard
    A = list(map(int, input().split()))
    
    # Initialisation du signe du produit (1 pour positif, -1 pour négatif)
    s = 1
    for i in A:
        # Inverser le signe si l'élément est négatif
        if i < 0:
            s *= -1
    
    # Calcul de la liste des valeurs absolues
    Aabs = list(map(abs, A))
    
    # Si le produit global est positif ou nul, on affiche la somme directe
    if s == 1:
        print(sum(Aabs))
    # Sinon, il faut soustraire deux fois la plus petite valeur absolue
    else:
        print(sum(Aabs) - 2 * min(Aabs))

# Appel de la fonction principale si ce script est exécuté
if __name__ == "__main__":
    calculate_special_sum()