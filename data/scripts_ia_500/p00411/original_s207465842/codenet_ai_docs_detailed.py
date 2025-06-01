def calculate_ratio_time(a, t, r):
    """
    Calcule le produit du temps t par le ratio r divisé par a.
    
    Args:
        a (int): Le diviseur utilisé dans le calcul du ratio.
        t (int): La variable temps multipliée par le ratio.
        r (int): Le numérateur utilisé dans le calcul du ratio.
    
    Returns:
        float: Le résultat de (r / a) * t.
    """
    return (r / a) * t

# Lecture de trois entiers séparés par un espace depuis l'entrée standard
a, t, r = [int(x) for x in input().split(" ")]

# Calcul du résultat en utilisant la fonction définie précédemment
result = calculate_ratio_time(a, t, r)

# Affichage du résultat calculé
print(result)