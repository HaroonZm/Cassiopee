# La boucle while True démarre une boucle infinie.
# Cette boucle continuera encore et encore jusqu'à ce qu'elle rencontre une instruction break.
while True:
    # Ici, la fonction input() attend que l'utilisateur fournisse une ligne de texte.
    # Cette entrée devrait contenir deux nombres entiers séparés par un espace.
    # La méthode split() sépare cette ligne en deux parties (sous forme de chaînes).
    # La fonction map() convertit ces deux chaînes en entiers.
    # L'instruction multiple (N, M =) permet d'assigner séparément les deux valeurs à N et M.
    N, M = map(int, input().split())

    # Le symbole | est l'opérateur OU bit à bit.
    # (N | M) évalue à 0 uniquement si N == 0 et M == 0.
    # Donc, si les deux valeurs sont 0, la condition est vraie et on exécute break pour sortir de la boucle.
    if (N | M) == 0:
        break

    # input() lit la prochaine ligne, qui doit contenir des entiers séparés par des espaces.
    # .split() sépare cette ligne en une liste de chaînes.
    # La compréhension de liste parcourt chaque string (x) dans la liste, et la convertit en int.
    # Cela donne une nouvelle liste d'entiers stockée dans la variable A.
    A = [int(x) for x in input().split()]

    # On initialise une variable entière ans à 0.
    # Cette variable va servir à accumuler une somme au fur et à mesure.
    ans = 0

    # // représente la division entière (= division dont le résultat est arrondi à l'entier inférieur).
    # M est divisé par N, et on remplace M par ce nouveau résultat.
    M //= N

    # On démarre une boucle for, qui va examiner chaque élément a de la liste A.
    for a in A:
        # On compare a (un élément de la liste A) à la valeur M.
        # Si a est strictement inférieur à M, on ajoute a à la variable ans.
        if a < M:
            ans += a
        # Sinon (donc si a est supérieur ou égal à M) :
        else:
            # On ajoute la valeur M à ans.
            ans += M

    # On affiche la somme finale accumulée dans la variable ans, avec la fonction print().
    print(ans)