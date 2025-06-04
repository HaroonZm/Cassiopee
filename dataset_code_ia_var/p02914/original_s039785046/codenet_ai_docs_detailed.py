def get_basis(a):
    """
    Calcule la base linéaire de l'ensemble des entiers fournis sur le corps GF(2).
    La base retournée est une base réduite telle que tout élément du sous-espace vectoriel 
    généré par 'a' peut s'écrire comme combinaison linéaire (XOR) des éléments de la base.

    Args:
        a (list of int): Liste d'entiers pour laquelle calculer la base linéaire (modulo 2).
    
    Returns:
        list of int: La base réduite, où chaque élément est linéairement indépendant (modulo 2).
    """
    basis = []  # Liste qui va contenir les éléments de la base
    for e in a:
        # Pour chaque nouvel élément, on le réduit vis-à-vis des éléments déjà dans la base
        for b in basis:
            # On remplace 'e' par le minimum avec 'e XOR b' pour garantir l'aspect réduit
            e = min(e, e ^ b)
        if e:
            # Si 'e' est non nul après réduction, il est linéairement indépendant, on l'ajoute à la base
            basis.append(e)
    return basis

def main():
    """
    Fonction principale qui lit les entrées, effectue les transformations, et affiche le résultat.
    Procède comme suit :
    1. Lit 'n' et la liste 'a'.
    2. Calcule le XOR de toute la liste (forte contribution au résultat final).
    3. Filtre chaque élément pour annuler les bits déjà présents dans 'ans' (le XOR total).
    4. Calcule la base linéaire des éléments filtrés.
    5. Cherche le plus grand XOR possible obtenu en combinant des éléments de la base.
    6. Affiche le résultat final.
    """
    
    # Lecture de la taille du tableau
    n = int(input())
    # Lecture des éléments du tableau
    a = list(map(int, input().split()))
    
    # Calcul du XOR total de la liste; c'est la contribution initiale au résultat
    ans = 0
    for i in a:
        ans ^= i

    # Calcul du masque complémentaire : ~ans. Les bits à 1 dans ce masque indiquent les positions où l’on veut maximiser le XOR restant.
    k = ~ans
    
    # Filtrage des éléments : on garde uniquement les bits que l’on peut potentiellement augmenter (non présents dans ans)
    for i in range(n):
        a[i] &= k

    # Construction de la base linéaire des éléments devant être XOR-és pour maximiser le résultat
    basis = get_basis(a)
    
    # Calcul du meilleur XOR possible avec la base (maximum sur tous les XOR de sous-ensembles)
    res = 0
    for i in basis:
        # On tente d'améliorer res en xorant avec chaque base
        res = max(res, res ^ i)
    
    # Affichage du résultat final: le XOR initial + deux fois le maximum ajouté grâce à la base linéaire
    print(ans + 2 * res)

# Appel de la fonction principale
main()