def main():
    """
    Lit une chaîne de caractères représentant une séquence de rainures, bâcles et plats,
    calcule l'aire totale piégée par les bâcles (water trapping problem) et donne le détail des "trous".
    Entrée: une chaîne composée de "\" et "/" (par exemple: \\///\_/\/) saisie par l'utilisateur.
    Sorties:
      - affiche l'aire totale piégée (entier)
      - affiche le nombre de trous puis la taille de chaque trou, ou 0 en l'absence de trou
    """
    A = []   # Pile pour stocker les indices des barres descendantes ("\")
    p = []   # Liste des tuples (indice_gauche, surface) pour chaque "trou" détecté
    a = 0    # Surface totale cumulée piégée par les bâcles
    i = 0    # Position courante dans la chaîne (servira d'indice)

    # Parcours caractère par caractère de l'entrée utilisateur
    for c in input():
        if c == "\\":  # Si on rencontre une descente, on stocke l'indice courant
            A.append(i)
        elif c == "/" and A:  # Si on remonte et qu'il y a une descente disponible
            j = A.pop()  # On récupère l'indice du dernier "\"
            t = i - j    # Surface entre la descente et la montée
            a += t       # On ajoute la surface à la surface totale

            # Regroupement des éventuelles zones contiguës déjà détectées et imbriquées
            while p and p[-1][0] > j:
                t += p[-1][1]  # On fusionne les surfaces si imbriquées
                p.pop()        # On retire les trous fusionnés

            p.append((j, t))   # On mémorise le trou courant avec sa surface
        i += 1  # Passage au caractère suivant

    print(a)  # Affichage de la surface totale piégée

    if p:
        # On affiche le nombre de trous puis la taille de chacun (dans l'ordre du graphique)
        print(len(p), *[t[1] for t in p])
    else:
        # Aucun trou détecté
        print(0)

if __name__ == "__main__":
    main()