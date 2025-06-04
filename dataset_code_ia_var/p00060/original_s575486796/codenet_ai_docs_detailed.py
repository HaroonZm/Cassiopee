import sys

# Raccourcis pour la lecture et l'écriture standard
readlines = sys.stdin.readlines
write = sys.stdout.write

def solve():
    """
    Lit chaque ligne de l'entrée standard. Pour chaque ligne contenant trois entiers a, b et c,
    détermine s'il existe un nombre suffisant de troisièmes cartes (x) non choisies parmi 1..10
    telles que la somme a + b + x ne dépasse pas 20.

    Si le nombre de possibilités multiplié par 2 est strictement supérieur à 7, affiche 'YES',
    sinon affiche 'NO'.
    """
    # Parcourt chaque ligne de l'entrée standard
    for line in readlines():
        # Initialise un tableau de taille 11 pour marquer les cartes choisies (indices 1 à 10)
        U = [0] * 11
        # Extrait les trois cartes choisies
        a, b, c = map(int, line.split())
        # Marque les cartes a, b et c comme déjà utilisées
        U[a] = U[b] = U[c] = 1
        res = 0  # Compteur du nombre de cartes valides
        # Parcourt toutes les valeurs possibles pour la troisième carte x, de 1 à 10
        for x in range(1, 11):
            # Ignore les cartes déjà utilisées
            if U[x]:
                continue
            # Vérifie si la somme des trois cartes ne dépasse pas 20
            if a + b + x <= 20:
                res += 1
        # Si le nombre de choix valides multiplié par 2 est strictement supérieur à 7, écrit "YES"
        if res * 2 > 7:
            write("YES\n")
        else:
            write("NO\n")

# Appel de la fonction principale pour démarrer le traitement
solve()