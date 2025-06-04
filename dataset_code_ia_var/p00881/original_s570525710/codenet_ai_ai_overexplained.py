from collections import Counter  # Importe la classe Counter du module collections pour compter facilement les éléments

while True:  # Crée une boucle infinie, qui ne se termine que lorsqu'on l'arrête explicitement avec 'break'
    # Lit une ligne de l'entrée standard, la découpe en morceaux par les espaces, et convertit chaque morceau en entier
    m, n = (int(s) for s in input().split())
    # Si m vaut zéro, cela signifie que l'on doit arrêter la boucle (condition d'arrêt du problème)
    if not m:
        break

    # Crée une liste 'objs' contenant 'n' entiers
    # Chaque entier est lu sur une nouvelle ligne, lu comme une chaîne binaire ('input()'), puis converti en int en base 2
    objs = [int(input(), 2) for i in range(n)]

    # Initialise une table 'dp', qui est une matrice à deux dimensions de taille (2^m) x (2^m)
    # Chaque élément est initialisé à zéro
    # 'dp[mask][masked]' servira à mémoriser des sous-résultats pour différentes combinaisons de bits
    dp = [[0] * (1 << m) for i in range(1 << m)]

    # Crée une liste 'bits' contenant des puissances de deux correspondant à chaque bit de 0 à m-1
    # Cela permet de manipuler facilement chaque bit individuellement
    bits = [1 << i for i in range(m)]

    # Parcours tous les entiers de 2^m-1 jusqu'à 0, donc toutes les combinaisons de bits possibles
    # 'mask' représente un ensemble de bits marqués comme "déjà utilisés"
    for mask in reversed(range(1 << m)):
        # Pour chaque objet dans 'objs', effectue un 'AND' bit à bit entre l'objet et 'mask'
        # Compte combien de fois chaque résultat apparaît à l'aide de Counter
        s = Counter(obj & mask for obj in objs)
        # Parcours tous les 'masked' (les résultats uniques de 'obj & mask') et le nombre d'occurrences associé
        for masked, value in s.items():
            # Si au moins deux objets partagent ce même motif (ie. value > 1), alors il y a ambiguïté à lever
            if value > 1:
                # Pour chaque bit 'b' qui n'est pas encore sélectionné dans 'mask'
                # Pour chaque telle possibilité, prend le maximum entre :
                #   - 'dp[mask | b][masked]' : où on ajoute le bit 'b' au 'mask', mais pas au 'masked'
                #   - 'dp[mask | b][masked | b]' : où on ajoute le bit 'b' au 'mask' et au 'masked' (donc on révèle ce bit pour ce groupe)
                # Ajoute un coût de 1 (puisque l'on un révèle un nouveau bit)
                # On prend le minimum entre toutes ces possibilités
                dp[mask][masked] = min(
                    max(
                        dp[mask | b][masked],        # Cas où le bit 'b' n'est pas activé dans le 'masked' mais l'est dans le 'mask'
                        dp[mask | b][masked | b]    # Cas où le bit 'b' est activé dans les deux
                    ) + 1                          # On ajoute 1 car on vient de prendre une décision supplémentaire
                    for b in bits if not b & mask  # On ne considère que les bits qui ne sont pas déjà sélectionnés (b & mask == 0)
                )
    # Affiche le résultat stocké dans 'dp[0][0]'
    # Cela correspond au cas où aucun bit n'a encore été choisi ni révélé
    print(dp[0][0])