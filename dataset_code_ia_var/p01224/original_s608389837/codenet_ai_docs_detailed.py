def div(n):
    """
    Effectue la décomposition en facteurs premiers de n et calcule la somme de tous les diviseurs de n.

    La fonction retourne la somme de tous les diviseurs de n, en utilisant la décomposition en facteurs
    premiers et la formule :
        Si n = p1^k1 * p2^k2 * ... * pr^kr alors
        somme_diviseurs(n) = Π_i [ (p_i^(k_i+1) - 1) // (p_i-1) ]
    Args:
        n (int): Le nombre dont on cherche la somme des diviseurs.

    Returns:
        int: La somme de tous les diviseurs de n.
    """
    ls = []  # Liste pour stocker les facteurs premiers et leurs exposants
    i = 2    # Début de la recherche des facteurs premiers à partir de 2
    orig_n = n  # Sauvegarde la valeur initiale pour les tests
    while i * i <= n:
        c = 0  # Compteur de l'exposant du facteur premier i
        if n % i == 0:
            # Tant que i divise n, augmente l'exposant et divise n par i
            while n % i == 0:
                n //= i
                c += 1
        if c > 0:
            # Si i est un facteur premier de n, l'ajouter à la liste
            ls.append([i, c])
        i += 1
    if n > 1:
        # Si il reste un facteur premier > racine de n (n est alors premier)
        ls.append([n, 1])
    ans = 1  # Initialisation du produit pour la somme des diviseurs
    for b, p in ls:
        # Pour chaque facteur premier b d'exposant p, applique la formule de la somme des diviseurs
        ans *= (b ** (p + 1) - 1) // (b - 1)
    return ans

def main():
    """
    Boucle principale qui lit des entiers depuis l'entrée standard (jusqu'à ce que 0 soit entré),
    applique la fonction div() pour déterminer si chaque nombre est parfait, déficient ou abondant,
    puis affiche le résultat approprié.
    """
    while True:
        try:
            n = int(input())
        except (EOFError, ValueError):
            # Arrêt en cas de fin de fichier ou d'entrée invalide
            break
        if n == 0:
            # Met fin à la boucle si l'entrée est zéro
            break
        d = div(n) - n  # Calcul de la somme propre des diviseurs de n (excluant n lui-même)
        if d == n:
            print("perfect number")
        elif d < n:
            print("deficient number")
        else:
            print("abundant number")

if __name__ == "__main__":
    main()