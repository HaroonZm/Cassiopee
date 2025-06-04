# Boucle principale utilisant 'iter' pour lire des entrées jusqu'à ce que la valeur '0 0 0' soit fournie.
# 'iter(input, '0 0 0')' crée un itérable d'appels à 'input()', qui s'arrête quand '0 0 0' est lu.
for e in iter(input, '0 0 0'):
    # Transforme la chaîne d'entrée 'e' en liste de chaînes via 'split()' (sépare espaces).
    # Convertit chaque élément en entier avec 'map(int, ...)'.
    # Calcule la somme des entiers dans l'entrée, puis fait '-~sum' :
    # - L'opérateur un arithmétique '~' donne -(n+1), donc '-~n' donne n+1 (incrémente n de 1).
    n = sum(map(int, e.split()))
    taille_tableau = -~n  # Même chose que n + 1, car l'indice 0 n'est pas utilisé.
    # Crée une liste 'd' initialisée avec la valeur 2 pour chaque case (taille = n + 1).
    # Cela représente probablement l'état de n objets, cases 1 à n.
    d = [2] * taille_tableau

    # Crée une liste vide 'f', qui stockera certaines contraintes à vérifier plus tard.
    f = []

    # Pour toutes les lignes suivantes (correspond à int(input()): le nombre de contraintes).
    for _ in [0] * int(input()):
        # Lit une ligne de 4 entiers, qui représentent probablement une contrainte sur trois objets.
        s, t, u, v = map(int, input().split())

        # Si v n'est pas nul (ie v==1), alors on applique une règle : on met d[s], d[t] et d[u] à 1.
        # (Peut-être qu'ils sont marqués comme "bons" contraintes absolues.)
        if v:
            d[s] = d[t] = d[u] = 1
        else:
            # Sinon, on ajoute ce triplet (s,t,u) à la liste 'f', pour traitement ultérieur.
            f += [(s, t, u)]

    # Maintenant, on traite chaque contrainte dans 'f' (celle qui avait v==0).
    for s, t, u in f:
        # Produit d[t]*d[u]==1 : cela signifie que t et u sont tous deux "bons" (d[..]==1)
        # Si tel est le cas, alors s ne peut être bon, donc d[s]=0.
        if d[t] * d[u] == 1:
            d[s] = 0  # Marque s comme "mauvais" (d[s]=0)

        # Idem en permutant (si u et s sont bons, t devient mauvais)
        if d[u] * d[s] == 1:
            d[t] = 0

        # Idem pour (s, t, u, si s et t sont bons, u devient mauvais)
        if d[s] * d[t] == 1:
            d[u] = 0

    # À la fin de toutes les contraintes, affiche les valeurs de d[1] à la fin (on ignore d[0]).
    # '*d[1:]' déplie la liste pour afficher chaque valeur sur sa propre ligne (sep='\n').
    print(*d[1:], sep='\n')