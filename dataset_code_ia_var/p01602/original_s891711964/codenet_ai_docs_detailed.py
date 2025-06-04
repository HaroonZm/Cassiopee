def check_bracket_sequence():
    """
    Lit une séquence d'opérations sur des parenthèses et vérifie si la séquence est valide.
    Une séquence est valide si, à chaque étape, le nombre de parenthèses fermantes ne dépasse pas celui des ouvrantes,
    et si, à la fin, le total est équilibré (autant d'ouvrantes que de fermantes).

    Entrée :
        n (int) : nombre d'opérations à traiter
        Ensuite, pour n lignes, chacune comprend :
            p (str) : le type d'opération, soit '(' (ouvrir des parenthèses), soit ')' (fermer des parenthèses)
            x (int) : nombre de parenthèses à ouvrir ou à fermer

    Sortie :
        "YES" si la séquence est valide et équilibrée, "NO" sinon.
    """
    n = int(input())  # Lecture du nombre d'opérations à exécuter
    b = 0             # Compteur d'équilibre des parenthèses (solde d'ouvrantes - fermantes)
    ans = True        # Indicateur de validité de la séquence

    for _ in range(n):
        # Lecture de l'opération et conversion du nombre de parenthèses à traiter
        p, x = input().split()
        x = int(x)

        if p == "(":  # Si c'est une parenthèse ouvrante
            b += x    # On ajoute x au compteur
        else:         # Sinon, c'est une parenthèse fermante
            b -= x    # On enlève x au compteur
            if b < 0:
                # Si à un moment il y a plus de fermantes que d'ouvrantes, la séquence est invalide
                ans = False

    if ans:
        # Si tout s'est bien passé sans déséquilibre négatif
        if b == 0:
            # Si le solde final est 0, la séquence est correctement équilibrée
            print("YES")
        else:
            # Sinon, il manque ou il y a trop de parenthèses ouvrantes ou fermantes
            print("NO")
    else:
        # Si la séquence n'a pas toujours été valide
        print("NO")

# Exécution de la fonction principale
check_bracket_sequence()