def process_parentheses():
    """
    Gère un compteur basé sur les instructions de l'utilisateur pour déterminer
    si la somme courante des ouvertures et fermetures de parenthèses équilibre
    parfaitement après chaque instruction.

    À chaque étape :
    - 'a' : une valeur ignorée (peut être un identifiant ou autre donnée).
    - 'c' : un caractère, '(' pour ajouter, ')' pour soustraire.
    - 'n' : un entier, le nombre d'occurrences à ajouter ou soustraire.

    Affiche "Yes" si le compteur total est nul, "No" sinon.
    """
    cnt = 0  # Initialise le compteur total à zéro

    # Lit le nombre total d'instructions à traiter depuis l'entrée standard
    num_loops = int(raw_input())

    # Parcourt chaque instruction fournie par l'utilisateur
    for loop in xrange(num_loops):
        # Lit l'instruction et la sépare en parties
        a, c, n = raw_input().split()
        n = int(n)  # Convertit 'n' en entier

        # Met à jour le compteur selon le type de parenthèse
        if c == "(":
            cnt += n  # Ajoute 'n' au compteur si c'est '('
        else:
            cnt -= n  # Soustrait 'n' du compteur sinon

        # Affiche "Yes" si le compteur est à zéro, "No" sinon
        if cnt == 0:
            print "Yes"
        else:
            print "No"

# Appel de la fonction principale pour démarrer le programme
process_parentheses()