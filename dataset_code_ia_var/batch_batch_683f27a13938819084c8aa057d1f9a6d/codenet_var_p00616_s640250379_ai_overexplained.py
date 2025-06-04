import sys  # Importe le module sys, qui fournit l'accès à certaines variables et fonctions utilisées ou maintenues par l'interpréteur Python.
from sys import stdin  # Importe stdin (entrée standard) depuis le module sys, ce qui permet de lire les données qui sont entrées par l'utilisateur ou un fichier.
input = stdin.readline  # Redéfinit la fonction input pour lire une ligne depuis l'entrée standard avec readline, une façon efficace pour lire de grandes entrées.

# Contexte : 
# Le but du programme est de traiter plusieurs jeux de données. 
# Chaque jeu correspond à un cube de taille n x n x n (3D), 
# et différentes tranches (planes) de ce cube sont spécifiées comme "trouées". 
# On doit déterminer combien de petits cubes (unités) sont complètement "trouées" au total.

# Le programme fonctionne en boucle pour traiter tous les jeux de données jusqu'à ce que n == 0.
while True:
    # Lit une ligne de l'entrée, la découpe en chaînes, puis les convertit en entiers pour n et h.
    n, h = map(int, input().split())  # n : taille du cube, h : nombre de plans troués
    if n == 0:
        # S'il n'est plus demandé de traiter de cubes (n=0), on quitte la boucle principale.
        break

    ans = []  # Initialise une liste vide qui contiendra des entiers représentant coordonnées 3D aplatées.

    # Pour chaque plan troué (h descriptions à lire) :
    for i in range(h):
        # Lit une ligne décrivant un plan : c (type du plan), a et b (coordonnées du plan)
        c, a, b = input().split()  # c : chaîne "xy", "xz", ou "yz", a et b des entiers sous forme de chaînes

        # Convertit a et b depuis une base humaine (1-based) à base informatique (0-based)
        a, b = int(a) - 1, int(b) - 1

        # Pour chaque type de plan, on marque tous les petits cubes concernés par ce "trou"
        if c == "xy":
            # Si le plan est parallèle à l'axe Z, ses coordonnées "a" et "b" fixent les axes X et Y.
            # On parcourt chaque valeur possible de Z (de 0 à n-1) pour ce plan.
            # Le cube est plat sur XY avec la coordonnée Z variant, donc coordonnées (a, b, z)
            # Pour représenter de façon unique chaque cube, les coordonnées x, y, z sont a, b, z
            # Pour transformer (x, y, z) en un entier unique, on utilise : ID = x + y * n + z * n * n
            # Mais ici, décalages utilisés sont : x + (y << 9) + (z << 18), comme n <= 500 < 512, donc 9 bits suffisent.
            ans += [a + (b << 9) + (z << 18) for z in range(n)]
        elif c == "xz":
            # Si le plan est parallèle à l'axe Y, les coordonnées "a" et "b" fixent X et Z.
            # On parcourt chaque valeur de Y (de 0 à n-1)
            # Donc les coordonnées sont (a, y, b), x = a, y varie, z = b
            ans += [a + (y << 9) + (b << 18) for y in range(n)]
        else:
            # Dernier cas : c == "yz"
            # Le plan est parallèle à l'axe X, les coordonnées "a" et "b" fixent Y et Z.
            # On parcourt chaque valeur de X (de 0 à n-1)
            # Les coordonnées sont (x, a, b), y = a, z = b
            ans += [x + (a << 9) + (b << 18) for x in range(n)]

    # À ce stade, ans contient tous les cubes troués (mais certains peuvent l'être plusieurs fois, donc doublons)
    # On transforme la liste en set pour ne garder que les identifiants uniques des cubes troués.
    troued = set(ans)  # 'troued' contient tous les indices des petits cubes troués, sans doublon

    # Le nombre total de petits cubes dans un cube de taille n est n^3.
    total_cubes = n ** 3  # Calcule le nombre total de cubes élémentaires

    # On affiche la différence : total cubes moins ceux troués (c'est donc le nombre de cubes non troués)
    print(total_cubes - len(troued))  # Affiche le résultat pour ce jeu de données

# Fin du programme. L'entrée se poursuit jusqu'à ce que la ligne lue ait n=0, qui provoque la sortie de la boucle.