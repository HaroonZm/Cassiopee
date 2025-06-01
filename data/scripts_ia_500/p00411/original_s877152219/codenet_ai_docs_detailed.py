def calculer_resultat(a, t, r):
    """
    Calcule le résultat de l'expression r * t / a.

    Args:
        a (int): Le premier entier, utilisé comme dénominateur dans le calcul.
        t (int): Le second entier, utilisé comme multiplicateur dans le numérateur.
        r (int): Le troisième entier, également utilisé comme multiplicateur dans le numérateur.

    Returns:
        float: Le résultat du calcul r * t / a.
    """
    return r * t / a

# Lecture des trois entiers séparés par des espaces depuis l'entrée standard
a, t, r = list(map(int, input().split()))

# Calcul du résultat avec la fonction définie précédemment
ans = calculer_resultat(a, t, r)

# Affichage du résultat formaté avec 6 chiffres après la virgule
print("{:.6f}".format(ans))