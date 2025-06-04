def ext_gcd(a, b):
    """
    Calcule le PGCD de 'a' et 'b' ainsi que les coefficients de Bézout.

    Résout l'équation de Bézout : a*x + b*y = gcd(a, b)
    et retourne un tuple (x, y) tel que cette relation soit vérifiée.

    Args:
        a (int): Le premier entier.
        b (int): Le deuxième entier.

    Returns:
        tuple: Un couple d'entiers (x, y) vérifiant l'équation de Bézout.
    """
    # Cas de base : si b vaut 0, alors le PGCD est a, et la relation est a*1 + 0*0 = a
    if b == 0:
        return 1, 0
    # q est le quotient de la division entière de a par b, t est le reste
    q, t = divmod(a, b)
    # Appel récursif sur (b, t)
    x, y = ext_gcd(b, t)
    # Renvoie les coefficients ajustés pour l'étape courante
    return y, (x - q * y)

def main():
    """
    Fonction principale qui lit deux entiers en entrée,
    calcule le couple de coefficients de Bézout grâce au PGCD étendu,
    puis les affiche à l'écran.
    """
    # Lit deux entiers séparés par un espace depuis l'entrée standard
    a, b = map(int, input().split())
    # Appelle l'algorithme du PGCD étendu et affiche les résultats
    print(*ext_gcd(a, b))
    return

# Appelle la fonction principale si ce script est exécuté
main()