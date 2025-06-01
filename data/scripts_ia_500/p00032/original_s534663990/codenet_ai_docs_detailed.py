import sys

# Assign function references for efficient input reading and output writing
readlines = sys.stdin.readlines
write = sys.stdout.write

def solve():
    """
    Lit plusieurs lignes d'entrées standard, chacune contenant trois entiers séparés par des virgules.
    Pour chaque triplet (a, b, c), la fonction vérifie :
    - si (a, b, c) forme un triplet pythagoricien (a^2 + b^2 == c^2)
    - si les deux premiers entiers a et b sont égaux

    Elle compte le nombre de lignes satisfaisant à chacune de ces conditions.
    Enfin, elle affiche deux nombres :
    - le nombre de triplets pythagoriciens
    - le nombre de triplets où a == b
    """
    # Initialisation des compteurs pour les deux critères
    v1 = v2 = 0

    # Parcours de toutes les lignes fournies en entrée standard
    for line in readlines():
        # Suppression d'éventuels espaces et découpage des trois valeurs par la virgule
        a, b, c = map(int, line.split(","))

        # Vérification si a, b, c forme un triplet pythagoricien
        if a**2 + b**2 == c**2:
            v1 += 1  # Incrémentation du compteur pour les triplets pythagoriciens

        # Vérification si les deux premiers nombres sont égaux
        if a == b:
            v2 += 1  # Incrémentation du compteur pour a == b

    # Écriture du résultat : nombre de triplets pythagoriciens
    write("%d\n" % v1)
    # Écriture du résultat : nombre de lignes où a est égal à b
    write("%d\n" % v2)

# Appel de la fonction principale pour lancer le traitement
solve()