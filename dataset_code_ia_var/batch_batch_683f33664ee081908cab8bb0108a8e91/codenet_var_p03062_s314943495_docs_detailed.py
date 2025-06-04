def main():
    """
    Lit une séquence de nombres entiers, calcule la somme des valeurs absolues et ajuste la somme
    si le nombre de valeurs négatives est impair.

    Si le nombre de valeurs négatives est pair, la somme des valeurs absolues est affichée.
    Si ce nombre est impair, on soustrait deux fois la plus petite valeur absolue à la somme,
    ce qui correspond à retourner un nombre impair de signes négatifs pour minimiser la somme absolue.
    """
    # Lecture du nombre de valeurs à traiter
    n = int(input())
    # Lecture de la liste des entiers
    a = list(map(int, input().split()))

    # Comptage des nombres négatifs dans la liste
    cnt = sum(i < 0 for i in a)
    # Calcul de la somme des valeurs absolues des éléments
    ans = sum(abs(i) for i in a)
    if cnt % 2 == 0:
        # Si le nombre de négatifs est pair, aucune modification n'est nécessaire
        print(ans)
    else:
        # Si le nombre de négatifs est impair, on doit inverser le signe de l'élément de plus petite valeur absolue
        # pour obtenir un résultat optimal, donc on soustrait deux fois cette valeur minimale
        print(ans - 2 * min(abs(i) for i in a))

if __name__ == "__main__":
    main()