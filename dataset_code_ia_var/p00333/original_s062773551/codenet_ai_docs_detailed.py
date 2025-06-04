def sdk(a, b):
    """
    Calcule le plus grand commun diviseur (PGCD) de deux entiers à l'aide de l'algorithme d'Euclide récursif.
    
    Args:
        a (int): Le premier entier.
        b (int): Le deuxième entier.
    
    Returns:
        int: Le plus grand commun diviseur de a et b.
    """
    # Si a est inférieur à b, on échange les deux pour garantir que a >= b
    if a < b:
        a, b = b, a
    # Si a est divisible par b, alors b est le PGCD
    if a % b == 0:
        return b
    else:
        # Appel récursif avec b et le reste de a divisé par b
        return sdk(b, a % b)

# Lecture de l'entrée utilisateur : trois entiers séparés par des espaces
w, h, c = map(int, input().split())

# Calcul du PGCD de w et h pour trouver le plus grand côté commun
t = sdk(w, h)

# Calcul et affichage du résultat : nombre total de carreaux carrés de taille maximale multiplié par c
print(w // t * h // t * c)