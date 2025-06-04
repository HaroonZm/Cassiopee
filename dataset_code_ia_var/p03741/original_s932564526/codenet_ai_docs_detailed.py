"""
Ce programme trouve le coût minimal pour convertir une séquence d'entiers en une séquence dont la somme cumulée alterne entre positif et négatif (+, -, +, -, ... ou -, +, -, +, ...).
Il teste les deux possibilités d'alternance et affiche le coût minimum pour corriger la séquence initiale.
"""

# Lecture de la taille de la séquence
N = int(input())
# Lecture de la séquence d'entiers à partir de l'entrée standard
A = list(map(int, input().split()))

def solve(start_sgn):
    """
    Calcule le coût total pour transformer la séquence A en une séquence
    où la somme cumulée alterne en commençant par 'start_sgn' (+1 ou -1).

    Arguments :
        start_sgn (int): Le signe de départ de la somme cumulée (+1 ou -1)

    Retourne :
        int: Le coût total des modifications nécessaires
    """
    sgn = start_sgn  # Signe attendu à chaque étape (+1 ou -1)
    r = 0            # Coût total accumulé des corrections
    s = 0            # Somme cumulée en cours

    # Parcourt chaque élément de la séquence
    for a in A:
        s += a  # Met à jour la somme cumulée

        # Si la somme cumulée ne respecte pas le signe attendu
        if s * sgn <= 0:
            # Correction : calcule le décalage à appliquer pour que s prenne la valeur minimale correctement signée
            r += abs(s - sgn)
            s = sgn  # Met à jour explicitement la somme cumulée corrigée

        sgn *= -1  # Alterne le signe attendu pour la prochaine position

    return r

# Calcule le coût minimum en testant les deux alternances possibles (commencer par + ou -)
print(min(solve(1), solve(-1)))