def main():
    """
    Lis un entier n, puis n paires d'entiers (a, b). Calcule une somme 's' où, pour chaque paire (a, b),
    s'ajoute 2^(a+b). Ensuite, pour chaque puissance de deux présente dans la somme (bits à 1 dans 's'),
    affiche la position du bit et 0 (format : 'position 0').
    """
    # Lecture du nombre de paires à traiter
    n = int(input())
    # Initialisation de la somme totale
    s = 0

    # Boucle sur chaque paire d'entrées
    for _ in range(n):
        # Lecture des deux entiers sur une même ligne, puis conversion en int
        a, b = map(int, input().split())
        # Ajoute à 's' la valeur 2^(a + b), écrite comme un décalage de bits
        s += 1 << (a + b)

    # Initialisation de la position du bit
    i = 0
    # Liste pour stocker les positions des bits à 1 dans la somme 's'
    ans = []

    # Extraction des bits à 1 dans la représentation binaire de 's'
    while s:
        # Vérifie si le bit de poids faible est à 1
        if s & 1:
            # Si oui, ajoute sa position à la liste
            ans.append(i)
        # Décale tous les bits d'une position vers la droite
        s >>= 1
        # Incrémente l'indicateur de position
        i += 1

    # Affichage du résultat : pour chaque position de bit à 1, affiche "<position> 0"
    for e in ans:
        print(e, 0)

if __name__ == "__main__":
    main()