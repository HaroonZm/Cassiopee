import numpy as np

DEG = 16
MOD = 10 ** 9 + 7

# Pré-définit les coefficients pour les cas pairs et impairs
even_coef = np.array(
    [0, 530289159, 384702529, 781298570, 90480784, 891754269, 348592099, 833888760, 898908474,
     505425073, 312827475, 794140068, 663894405, 565007911, 300594255, 98196225], dtype=np.int64)
odd_coef = np.array(
    [0, 231379733, 814507152, 631092340, 912089085, 58225824, 706460451, 264043077, 508834119,
     558179703, 136167972, 662064550, 384875310, 496818569, 537065939, 98196225], dtype=np.int64)

def compute_result(n):
    """
    Calcule la valeur résultante pour une valeur donnée de n en fonction des coefficients prédéfinis.
    La fonction sélectionne des coefficients différents selon que n est pair ou impair, élève la valeur ajustée 
    à différentes puissances, puis calcule la somme pondérée modulo MOD.
    
    Args:
        n (int): L'entier d'entrée pour lequel effectuer le calcul.
        
    Returns:
        int: La valeur calculée, résidu modulo MOD.
    """
    if n % 2 == 0:
        # Si n est pair, m = n / 2 et on utilise les coefficients pairs
        m = n // 2
        coef = even_coef
    else:
        # Si n est impair, m = (n-1)/2 et on utilise les coefficients impairs
        m = (n - 1) // 2
        coef = odd_coef

    # Prépare un tableau pour stocker m^i (modulo MOD) pour i de 0 à DEG-1
    ms = np.ones(DEG, dtype=np.int64)
    for i in range(1, DEG):
        ms[i] = ms[i - 1] * m % MOD  # Puissance successive de m
    # Produit terme à terme des coefficients et des puissances, somme des résultats puis réduction modulo MOD
    ans = (ms * coef % MOD).sum() % MOD
    return ans

def main():
    """
    Fonction principale qui lit l'entrée, traite tous les cas de test et affiche les résultats.
    
    Lit d'abord le nombre de cas de test, puis pour chaque cas, lit la valeur de n, calcule le résultat
    et stocke dans une liste tampon. Enfin, affiche toutes les réponses séparées par des retours à la ligne.
    """
    # Lit le nombre de cas de test
    t = int(input())
    buf = []  # Liste pour stocker les résultats pour chaque cas
    for _ in range(t):
        n = int(input())
        # Calcul du résultat pour chaque n et stockage dans le tampon
        ans = compute_result(n)
        buf.append(ans)
    # Impression des résultats, un par ligne
    print('\n'.join(map(str, buf)))

if __name__ == "__main__":
    main()