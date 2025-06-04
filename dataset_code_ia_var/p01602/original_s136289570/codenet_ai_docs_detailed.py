def check_parenthesis_sequence():
    """
    Lit d'abord un entier depuis l'entrée standard, indiquant le nombre de lignes qui suivront.
    Pour chaque ligne, lit un symbole '(' ou ')' et un nombre.
    Additionne ou soustrait ce nombre à un compteur selon le symbole.
    Si à tout moment le compteur devient négatif, arrête l'analyse immédiatement.
    Affiche 'YES' si le compteur final est exactement 0, sinon affiche 'NO'.
    """

    a = 0  # Initialisation du compteur qui déterminera l'équilibre de la séquence

    n = int(input())  # Lecture du nombre total d'opérations

    for _ in range(n):
        b, c = input().split()  # Lecture du symbole et du nombre
        if b == '(':  # Si le symbole est une parenthèse ouvrante
            a += int(c)  # On ajoute la valeur associée
        else:  # Si le symbole est une parenthèse fermante
            a -= int(c)  # On soustrait la valeur associée

        if a < 0:  # Vérification de l'équilibre à chaque étape
            break  # Si le nombre de fermantes dépasse les ouvrantes, on interrompt la boucle

    # Si après toutes les opérations, a vaut 0, les parenthèses sont équilibrées
    print('NO' if a else 'YES')

# Appel de la fonction principale
check_parenthesis_sequence()