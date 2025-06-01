import bisect

def main():
    """
    Lit les entrées, traite les données pour déterminer la taille maximale
    d'une séquence respectant certaines contraintes basées sur des préfixes
    cumulés, et imprime le résultat.

    Fonctionnement général :
    - Lecture de m, n : m correspond au nombre d'éléments dans w, n au nombre d'éléments dans c.
    - Lecture de m tuples pour w : chaque tuple contient deux entiers.
    - Calcul des sommes cumulées pour les deux listes issues de w.
    - Lecture de n tuples pour c : chaque tuple contient deux entiers.
    - Utilisation d'une structure de dictionnaire pour suivre les sous-ensembles d'indices
      de c et le meilleur indice atteint dans les listes cumulées w, t.
    - Recherche via bisect pour déterminer l'extension maximale possible à chaque étape.
    - Calcul de la valeur maximale finale parmi tous les sous-ensembles.
    """
    # Lire deux entiers m (nombre d'éléments dans w) et n (nombre d'éléments dans c)
    m, n = map(int, input().split())

    # Lire m tuples, chacun contenant deux entiers, stockés dans une liste w sous forme de tuples
    w = [tuple(map(int, input().split())) for _ in range(m)]

    # Séparer la liste w en deux listes distinctes w et t (x et y des tuples), en décompressant avec zip
    w, t = map(list, zip(*w))

    # Calcul des sommes préfixées pour les listes w et t
    # Chaque élément i devient la somme de tous les éléments jusqu'à i inclus
    for i in range(1, m):
        w[i] += w[i - 1]
        t[i] += t[i - 1]

    # Lire n tuples, chacun contenant deux entiers, stockés dans une liste c sous forme de tuples
    c = [tuple(map(int, input().split())) for _ in range(n)]

    # Séparer la liste c en deux listes distinctes c et b
    c, b = map(list, zip(*c))

    # Initialiser un dictionnaire a où la clé est un tuple contenant tous les indices [0, 1, ..., n-1]
    # et la valeur associée est -1, indiquant aucun élément atteint
    a = {}
    a[tuple(range(n))] = -1

    # Boucle principale s'exécutant n fois, traitant la réduction progressive des sous-ensembles d'indices
    for _ in range(n):
        # Créer une liste an contenant les paires (sous-ensemble d'indices, valeur atteinte) du dictionnaire a
        an = [(k, a[k]) for k in a]
        a = {}

        # Pour chaque élément (x) du tuple an : x[0] est le tuple des indices restants, x[1] la valeur maximale atteinte
        for x in an:
            for p in x[0]:  # Pour chaque indice p dans le tuple des indices restants
                # Calculer la nouvelle position i :
                # On cherche l'indice maximal i dans les cumuls w et t qui respecte une contrainte basée sur c[p], b[p]
                if x[1] != -1:
                    # Si un indice précédent existe, on décale par les valeurs aux indices x[1]
                    i = min(
                        bisect.bisect_right(w, c[p] + w[x[1]], x[1]),
                        bisect.bisect_right(t, b[p] + t[x[1]], x[1])
                    ) - 1
                else:
                    # Sinon, on cherche l'indice dans w et t sans décalage
                    i = min(
                        bisect.bisect_right(w, c[p]),
                        bisect.bisect_right(t, b[p])
                    ) - 1

                # Créer une nouvelle liste y en supprimant l'indice p des indices restants
                y = list(x[0])
                y.remove(p)
                y = tuple(y)

                # Mettre à jour le dictionnaire a pour la nouvelle clé y avec la valeur i,
                # en conservant la valeur maximale si déjà présente
                if y in a:
                    a[y] = max(a[y], i)
                else:
                    a[y] = i

    # Afficher le maximum des valeurs dans le dictionnaire a incrémenté de 1
    # Correspond au plus grand indice accessible + 1, potentiellement la taille maximale
    print(max([a[i] for i in a]) + 1)

if __name__ == "__main__":
    main()