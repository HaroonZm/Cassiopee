def compute_expression(N, d1, xx):
    """
    Calcule une expression complexe basée sur les entrées :
    N : entier, nombre d'itérations dans la boucle principale.
    d1 : float/int, valeur initiale pour 'd'.
    xx : float/int, valeur initiale pour 'x'.
    
    Retourne le résultat final formaté comme une chaîne à 12 décimales près.
    """
    # Initialisation des valeurs en flottant pour éviter la troncature entière
    d = float(d1)
    x = float(xx)
    res = 0.0  # Initialisation de la variable de résultat qui va accumuler la somme calculée

    # Boucle principale : tant que N > 1, itère le calcul demandé
    while N > 1:
        # Ajoute pour chaque itération la valeur calculée d'après la formule donnée :
        # (2*d + (2*N-1)*x) / 2
        res += (2*d + (2*N-1)*x) / 2

        # Mise à jour de 'd' selon la progression :
        d *= 1.0 + 1.0 / N   # 'd' est augmenté proportionnellement à 1/N
        d += x * 5.0/(2*N)   # puis on ajoute x * (5/2N) à 'd'

        # Mise à jour de 'x' selon la formule :
        x *= 1.0 + 2.0 / N   # 'x' est augmenté proportionnellement à 2/N

        N -= 1  # décrémente N pour la prochaine itération

    # Retourne le résultat total en ajoutant à la somme accumulée 'd' et la moitié de 'x'.
    # Résultat formaté avec 12 chiffres après la virgule.
    return "{:.12f}".format(res + d + x/2)


def main():
    """
    Fonction principale : lit trois entiers depuis l'entrée,
    appelle la fonction de calcul et affiche le résultat.
    """
    # Lecture des entrées utilisateur sous forme de trois entiers séparés par des espaces.
    N, d1, xx = map(int, raw_input().split())
    
    # Appel de la fonction de calcul et affichage du résultat.
    print compute_expression(N, d1, xx)


# Lancement du programme
if __name__ == '__main__':
    main()