# Lecture de deux entiers à partir de l'entrée utilisateur séparés par un espace
# La fonction input() permet de lire une ligne en entrée
# La méthode split() divise cette ligne en une liste de chaînes de caractères
# La fonction map(int, ...) convertit chaque chaîne en entier
# Enfin, on assigne ces deux valeurs à n et m, respectivement
n, m = map(int, input().split())

# Lecture de m entiers à partir de la deuxième entrée utilisateur
# split() divise la ligne en éléments, int(y) convertit chaque élément en entier
# L'expression [int(y) for y in input().split()] crée une liste d'entiers appelée x
x = [int(y) for y in input().split()]

# La méthode sort() trie la liste x par ordre croissant sur place
x.sort()

# Si le nombre de groupes souhaité (n) est supérieur ou égal au nombre total d'éléments (m)
if n >= m:
    # Il n'y a aucun coût (aucune différence à couvrir), il suffit d'imprimer 0
    print('0')
else:
    # Sinon, on initialise une liste vide y qui contiendra les différences consécutives entre les éléments de x
    y = []
    # La boucle for parcourt les indices de 0 à m-2 (inclus, car range(m-1))
    # Pour chaque indice i, on calcule la différence entre l'élément suivant et l'actuel, c'est-à-dire x[i+1] - x[i]
    # On ajoute cette différence à la liste y
    for i in range(m-1):
        y.append(x[i+1] - x[i])

    # On trie ensuite la liste y, qui contient maintenant toutes les différences consécutives, du plus petit au plus grand
    y.sort()

    # On initialise la variable ans avec la somme de toutes les différences consécutives stockées dans y
    # sum(y) additionne tous les éléments de y
    ans = sum(y)

    # Maintenant, nous voulons former n groupes. Pour cela, on enlève les n-1 plus grandes différences
    # La boucle for va donc de 0 à n-2 (inclus)
    for i in range(n-1):
        # y[-(i+1)] accède à l’i+1-ème élément depuis la fin de la liste (les plus grandes valeurs après tri)
        # ans -= ... signifie qu'on soustrait cette différence de la somme totale
        ans -= y[-(i+1)]

    # Enfin, on affiche la réponse finale qui est le coût minimal pour diviser x en n groupes consécutifs
    print(ans)