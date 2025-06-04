# Ce programme résout le problème AOJ 2800 "Mod!Mod!"
# Tout le code est commenté de manière extrêmement détaillée pour expliquer chaque aspect, même les bases.

# On lit d'abord un entier 'n' depuis l'entrée standard (input renvoie une chaîne, donc on convertit en entier avec int)
n = int(input())

# On lit la prochaine ligne d'entrée, qui est supposée contenir 'n' entiers séparés par des espaces.
# input() lit une chaîne, split() découpe la chaîne en morceaux selon les espaces, map(int, ...) convertit chaque sous-chaîne en entier.
# list(...) convertit l'objet map en liste Python contenant ces entiers.
a = list(map(int, input().split()))

# On crée une liste 'c' de 3 éléments, initialisée à 0. Cela sert à compter le nombre d'éléments dans chaque classe de reste modulo 3.
# c[0] comptera les valeurs dans 'a' qui sont divisibles par 3 (reste 0)
# c[1] comptera celles qui donnent un reste de 1 modulo 3
# c[2] comptera celles qui donnent un reste de 2 modulo 3
c = [0] * 3

# Pour chaque élément 'i' de la liste 'a':
for i in a:
    # On calcule le reste de 'i' par 3 (i % 3), ce reste sera soit 0, 1 ou 2
    # On utilise ce reste comme index de la liste 'c' et on incrémente le compteur correspondant de 1
    c[i % 3] += 1

# Après le comptage, c[0], c[1], c[2] contiennent le nombre de nombres avec restes 0, 1 et 2 respectivement.

# On vérifie ici si les deux valeurs c[1] et c[2] sont nulles.
# (c[1] | c[2]) est une opération OU au niveau des bits. Si les deux sont 0, le résultat est 0.
if (c[1] | c[2]) == 0:
    # Si c[1] == 0 et c[2] == 0, cela veut dire que tous les nombres sont divisibles par 3
    # La réponse est alors simplement 1 d'après l'énoncé du problème spécifique.
    ans = 1
else:
    # Sinon, on va calculer la réponse en fonction de la distribution des restes
    # On initialise 'ans' avec c[0], c'est-à-dire le nombre de nombres divisibles par 3
    ans = c[0]
    # On met à jour 'n' pour qu'il soit égal au nombre total d'éléments non divisibles par 3 :
    # c'est le nombre total 'n' moins ceux de reste 0, donc n - c[0]
    n = n - c[0]
    # Si les éléments restants n'excèdent pas 3, on peut tous les ajouter à 'ans'
    # (c'est un cas limite lié à la contrainte du problème)
    if n <= 3:
        ans += n
    else:
        # Sinon on doit équilibrer le nombre de restes 1 et 2 pour maximiser la solution
        # On calcule t = différence entre c[1] et c[2], mais bornée entre -3 et 3
        # max(-3, min(3, c[1]-c[2])) limite la différence pour éviter des valeurs trop grandes ou trop petites
        t = max(-3, min(3, c[1] - c[2]))
        # Si t > 0 cela veut dire qu'il y a plus de restes 1 que de restes 2 (environ)
        if t > 0:
            # ans est augmenté de 2*c[2] (on associe chaque reste 1 avec reste 2) puis on ajoute t
            ans += 2 * c[2] + t
        else:
            # Sinon, il y a plus de restes 2 ou équilibre parfait ; on traite symétriquement
            # On ajoute à ans : 2*c[1] (pour chaque 2 reste 1, il y a un reste 2 associé), moins t (t est négatif ou nul ici)
            ans += 2 * c[1] - t

# Enfin, on affiche la réponse avec print()
print(ans)