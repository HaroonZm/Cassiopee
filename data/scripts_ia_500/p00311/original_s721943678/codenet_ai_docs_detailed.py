h1, h2 = map(int, input().split())  
k1, k2 = map(int, input().split())  
a, b, c, d = map(int, input().split())  

def f(x, y):
    """
    Calcule un score basé sur deux entrées entières x et y,
    en utilisant des coefficients globaux a, b, c, d.

    Le calcul est :
        score = a*x + b*y + c*(x // 10) + d*(y // 20)

    Args:
        x (int): Première valeur entière.
        y (int): Deuxième valeur entière.

    Returns:
        int: Le score calculé selon la formule donnée.
    """
    return a * x + b * y + c * (x // 10) + d * (y // 20)

# Calcul des scores pour les deux paires de valeurs fournies en entrée
H = f(h1, h2)  # Score pour la première paire (h1, h2)
K = f(k1, k2)  # Score pour la deuxième paire (k1, k2)

# Détermination du résultat basé sur la comparaison des deux scores
ans = 'even'  # Valeur par défaut si les scores sont égaux
if H > K:
    ans = 'hiroshi'   # Si H est supérieur, le gagnant est 'hiroshi'
elif H < K:
    ans = 'kenjiro'   # Si K est supérieur, le gagnant est 'kenjiro'

# Affichage du résultat final
print(ans)