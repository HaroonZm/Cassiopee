# Demande à l'utilisateur de saisir une chaîne de caractères via le clavier.
# La fonction input() lit la saisie et la stocke dans la variable S.
S = input()  

# Initialise une variable entière n à 0.
# Cette variable n va servir de compteur pour suivre le nombre de parenthèses ouvrantes '(' rencontrées
# moins le nombre de parenthèses fermantes ')' rencontrées jusqu'à présent.
n = 0

# Initialise une variable entière ans à 0.
# Dans ce code donné, la variable ans n'est pas utilisée, mais elle pourrait servir à stocker un résultat à l'avenir.
ans = 0

# La boucle for va itérer (passer en revue) chaque caractère de la chaîne S, un à la fois.
# 'i' prend successivement toutes les valeurs (caractères) dans S.
for i in S:
    # Vérifie si le caractère courant 'i' est une parenthèse ouvrante '('.
    if i == "(":
        # Si c'est le cas, le compteur n est incrémenté de 1 (n = n + 1).
        # Cela signifie qu'on a rencontré une parenthèse ouvrante supplémentaire.
        n += 1
    # Sinon, vérifie si le caractère courant 'i' est une parenthèse fermante ')'.
    elif i == ")":
        # Si c'est le cas, le compteur n est décrémenté de 1 (n = n - 1).
        # Cela signifie qu'on a rencontré une parenthèse fermante qui "ferme" une parenthèse ouvrante précédente.
        n -= 1
    # Si le caractère courant n'est ni '(' ni ')', alors on entre dans le cas suivant (else).
    else:
        # Affiche la valeur actuelle de n en utilisant la fonction print().
        # Cela donne au programmeur ou à l'utilisateur une indication de l'état du compteur à ce moment précis.
        print(n)
        # Le mot-clé break arrête immédiatement la boucle for, même si tous les caractères de S n'ont pas encore été parcourus.
        break