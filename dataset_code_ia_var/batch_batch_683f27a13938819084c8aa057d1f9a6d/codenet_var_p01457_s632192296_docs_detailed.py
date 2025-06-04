def check_parentheses_balance():
    """
    Lit un nombre de lignes depuis l'entrée standard, puis pour chaque ligne :
      - Sépare la ligne en trois parties : un texte ignoré, un caractère de parenthèse ('(' ou ')') et un entier.
      - Ajoute ou soustrait cet entier à un compteur selon le caractère de parenthèse.
      - Affiche 'Yes' si, à ce moment, le compteur est exactement zéro (c'est-à-dire que les parenthèses sont équilibrées).
        Sinon, affiche 'No'.
    Aucune valeur n'est retournée. Les résultats sont imprimés à la sortie standard.
    """
    c = 0  # Compteur d'équilibre des parenthèses

    # Lecture du nombre de cas à traiter
    n = int(input())

    for _ in range(n):
        # Lecture et découpage de la ligne courante en trois variables
        # On ignore la première valeur '_', 's' est le type de parenthèse, 'a' représente un entier
        _, s, a = input().split()

        # Conversion de 'a' en entier
        a = int(a)

        # Mise à jour du compteur : on ajoute si '(', on soustrait si ')'
        if s == '(':
            c += a
        else:
            c -= a

        # Si le compteur est nul, les parenthèses sont équilibrées ('Yes'), sinon ('No')
        if c == 0:
            print('Yes')
        else:
            print('No')

# Appel de la fonction principale
check_parentheses_balance()