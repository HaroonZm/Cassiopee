# Boucle infinie, qui continuera à s'exécuter jusqu'à ce qu'une instruction de sortie soit rencontrée
while True:
    # Demande à l'utilisateur d'entrer une ligne de nombres séparés par des espaces, les convertit en entiers,
    # et calcule leur somme — ceci implique que l'utilisateur peut saisir plusieurs nombres, et map(int, ...)
    # applique int() à chaque entrée individuellement
    m = sum(map(int, input().split()))
    # Si la somme calculée m vaut zéro (c'est-à-dire qu'aucun nombre n'a été entré ou leur somme est 0),
    # alors on sort (break) de la boucle infinie ci-dessus, mettant fin au programme
    if not m:
        break
    # Demande à l'utilisateur d'entrer un nombre (attendu comme un entier) qui indique combien de lignes vont suivre
    n = int(input())
    # On crée une liste appelée 'fixed', qui comporte 'm' éléments, tous initialisés à la valeur 2.
    # Ici [2] * m signifie qu'on aura une liste de longueur m, chaque élément valant 2.
    fixed = [2] * m
    # On crée une liste vide 'failures' où nous stockerons ultérieurement des tuples — utilisé pour différer
    # le traitement si certains critères ne sont pas remplis
    failures = []
    # On commence une boucle for qui va s'exécuter 'n' fois, c'est-à-dire pour chaque ligne d'entrée à lire ensuite
    for _ in range(n):
        # Lit une ligne contenant quatre entiers séparés par des espaces, puis les attribue aux variables i, j, k, r.
        i, j, k, r = map(int, input().split())
        # On ajuste les indices de i, j, et k car les indices des listes Python commencent à 0, mais on suppose
        # que l'utilisateur entre des indices à partir de 1 (par exemple, 1 pour le premier élément)
        # On utilise ici une compréhension de générateur pour faire x-1 sur chaque valeur.
        i, j, k = (x - 1 for x in (i, j, k))
        # Si la variable r vaut quelque chose de non nul (c'est-à-dire si r est défini comme True ou 1 par exemple)
        if r:
            # On assigne la valeur 1 à chaque position correspondante dans la liste 'fixed'
            # Cela implique qu'il s'agit d'une "contrainte" active ou fixe pour ces indices
            fixed[i] = fixed[j] = fixed[k] = 1
        else:
            # Si r ne vaut pas True (autrement dit r == 0), alors on stocke ce triplet dans la liste 'failures'
            # pour un traitement ultérieur. La structure d'un triplet sera (i, j, k).
            failures.append((i, j, k))
    # Pour chaque triplet précédemment stocké dans 'failures', on effectue un traitement
    for i, j, k in failures:
        # On extrait la valeur actuelle de fixed à l'indice i, puis à l'indice j, puis à l'indice k
        # Cela permet de déterminer quel est l'état fixé (2, 1 ou 0) de chacun de ces indices
        fi, fj, fk = (fixed[x] for x in (i, j, k))
        # Si l'élément fi (index i dans fixed) est égale à 1, c'est-à-dire qu'il est fixé, alors:
        if fi == 1:
            # Si en plus fj (index j dans fixed) vaut également 1...
            if fj == 1:
                # ...alors on assigne la valeur 0 à fixed[k] (c'est-à-dire, l'élément à l'indice k)
                # On "exclut" donc k si i et j sont fixés à 1
                fixed[k] = 0
            # Sinon, si fk (index k dans fixed) est fixé à 1...
            elif fk == 1:
                # ...alors on assigne la valeur 0 à fixed[j], donc on "exclut" j
                fixed[j] = 0
        # Si i n'est pas fixé à 1 (fi != 1), mais à la fois fj et fk sont tous deux fixés à 1...
        elif fj == 1 and fk == 1:
            # ...alors on assigne la valeur 0 à fixed[i], donc on "exclut" i
            fixed[i] = 0
    # Affiche chaque valeur de la liste 'fixed' sur une nouvelle ligne.
    # '\n'.join(...) crée une chaîne où chaque élément de fixed est converti en une chaîne grâce à str(x),
    # et toutes ces chaînes sont jointes (concaténées) avec un saut de ligne entre elles.
    print('\n'.join(str(x) for x in fixed))