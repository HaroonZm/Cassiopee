def f(p):
    """
    Calcule la somme des diviseurs propres d'un nombre entier p.
    
    Args:
        p (int): Le nombre pour lequel calculer la somme des diviseurs propres.
        
    Returns:
        int: La somme des diviseurs propres de p (excluant p lui-même). 
             Retourne 0 si p est inférieur ou égal à 5.
    """
    ans = 1  # 1 est toujours un diviseur propre pour tout entier > 1
    if p <= 5:
        return 0  # Les nombres <= 5 n'ont pas de diviseurs propres autres que 1
    # Boucle sur tous les nombres possibles de 2 à sqrt(p)
    for n in range(2, int(p ** 0.5) + 1):
        if p % n == 0:  # Si n divise p
            if n != p // n:
                # n et p//n sont deux diviseurs distincts, les ajouter
                ans += n + p // n
            else:
                # n==p//n, cela se produit si n^2 == p (racine carrée parfaite)
                ans += n
    return ans

while True:
    # Demande un nombre à l'utilisateur
    n = int(input())
    # Si l'utilisateur saisit 0, on quitte la boucle
    if n == 0:
        break
    # Calcule la somme des diviseurs propres de n
    m = f(n)
    # Analyse et affiche la classification de n selon la somme de ses diviseurs propres
    if n == m:
        print('perfect number')  # Le nombre est parfait
    else:
        # On affiche 'deficient number' si la somme est inférieure à n, sinon 'abundant number'
        print('deficient number' if n > m else 'abundant number')