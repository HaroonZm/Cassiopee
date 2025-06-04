# Solution Python pour le problème Party Dress

# Le problème : Yae a A robes et B fêtes. Elle veut réduire au minimum possible
# la fréquence maximale d'utilisation d'une même robe, sachant qu'elle doit
# couvrir toutes les fêtes avec ses robes. Autrement dit, on cherche à minimiser
# le maximum d'utilisations d'une robe sachant qu'on a A robes et B utilisations à couvrir.

# Analyse :
# Chaque robe peut être utilisée un nombre certain de fois.
# Si on répartit les B fêtes sur A robes aussi uniformément que possible,
# alors la fréquence maximale d'utilisation d'une robe est le nombre entier
# minimal x tel que A*x >= B.
# En effet, si chaque robe est utilisée au maximum x fois,
# Le total de robes utilisables est A*x.
# On veut le plus petit x tel que A*x >= B.

# Cette valeur correspond donc au plafond de B / A.

def max_wear_frequency(A: int, B: int) -> int:
    """
    Calcule la fréquence maximale minimale à laquelle Yae doit porter la même robe.

    :param A: Nombre de robes disponibles.
    :param B: Nombre total de fêtes.
    :return: Fréquence maximale la plus basse possible de réutilisation d'une robe.
    """
    # Utilisation de la division entière avec arrondi supérieur
    # Pour calculer le plafond de B/A sans import de math
    return (B + A - 1) // A

# Lecture des entrées
A, B = map(int, input().split())

# Calcul du résultat
result = max_wear_frequency(A, B)

# Affichage du résultat
print(result)