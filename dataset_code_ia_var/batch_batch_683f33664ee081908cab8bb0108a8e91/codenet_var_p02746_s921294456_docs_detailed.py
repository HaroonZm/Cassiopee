def s(t, i):
    """
    Extrait le chiffre en base 3 à la position i d'un entier t (positions à partir de 0).
    
    Args:
        t (int): L'entier dont on veut extraire le chiffre.
        i (int): La position du chiffre à extraire en base 3 (0 pour le moins significatif).
        
    Returns:
        int: Le chiffre de l'entier t en base 3 à la position i.
    """
    # Pour extraire le chiffre, on effectue une division entière, puis on prend le reste par 3
    return 0 - -t // 3**i  # Équivaut à t // 3**i


def m(a, b, c, d):
    """
    Trouve le plus petit niveau 'i' d'une différence significative de position entre les points (a, b) et (c, d)
    dans le trajet d'un jeu particulier (probablement une structure en fractale type Sierpinski), selon certaines règles.
    
    Args:
        a (int): Première coordonnée horizontale.
        b (int): Première coordonnée verticale.
        c (int): Seconde coordonnée horizontale.
        d (int): Seconde coordonnée verticale.
        
    Returns:
        int: Le plus bas niveau 'i' + 1 respectant la condition, ou 0 s'il n'y en a pas.
    """
    # On cherche le dernier niveau (i) où :
    #  - les coordonnées horizontales a et c sont dans le même "bloc" base 3 au niveau i
    #  - la position mod 3 == 2 (cela sélectionne probablement des bords ou des coins)
    #  - il y a une différence verticale significative entre les couplages (b, d)
    niveaux = [
        i for i in range(30)
        if s(a, i) == s(c, i) and s(a, i) % 3 == 2 and 1 < abs(s(b, i) - s(d, i))
    ]
    # Si aucun niveau n'est trouvé, on retourne 0 (avec le +1 en sortie car on stocke -1 dans la liste par défaut)
    return max(niveaux + [-1]) + 1


def main():
    """
    Effectue les opérations principales pour chaque cas de test, lit 4 entiers à chaque entrée,
    calcule la valeur de transformation selon une fractale (ou grille), et affiche la distance minimale.
    
    Métaphores :
        Cette structure s'inspire probablement du déplacement dans la courbe de Sierpinski ou une fractale similaire.
    """
    # Traitement pour chaque cas de test
    for _ in [0] * int(input()):
        # Lecture des positions de départ et d'arrivée
        a, b, c, d = map(int, input().split())

        # Calcul du niveau critique horizontal et vertical pour le mouvement
        h = m(a, b, c, d)
        w = m(b, a, d, c)

        # Cas particulier : aucun piège fractal, chemin direct
        if h == w == 0:
            print(abs(b - d) + abs(a - c))
            continue

        # On veut que h soit toujours >= w en permutant si besoin
        if h < w:
            h, a, b, c, d = w, b, a, d, c

        # i représente la taille de la subdivision courante
        i = 3**h // 3
        # x est le centre relatif du bloc horizontal
        x = 2 * i + 1

        # Décalage pour recaler dans le "bloc milieu"
        g = a - (a - 1) % (3 * i) - 1
        a -= g
        c -= g

        # Calcul du résultat : distance verticale + minimum de l'accès au centre du bloc
        print(abs(b - d) + min(abs(i - a) + abs(i - c), abs(x - a) + abs(x - c)))


if __name__ == "__main__":
    main()