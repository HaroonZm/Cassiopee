from heapq import heappush, heappop  # Importer deux fonctions pour manipuler une structure de données spéciale appelée "tas" ou "heap" qui permet d'organiser et extraire rapidement les éléments selon leur ordre.

n = input()  # Lire une valeur depuis l'entrée standard (généralement le clavier), cette valeur représente un nombre d'itérations. Cette valeur est lue sous forme de chaîne de caractères.

n = int(n)   # Convertir cette chaîne de caractères en un entier, car on doit utiliser ce nombre dans une boucle qui nécessite un entier.

h = [-10000]*4  # Initialiser une liste appelée h de taille 4, remplie avec la valeur -10000. Ici, on prépare un tas avec quatre éléments, tous égaux à -10000. 
                # Cette liste servira à maintenir les 4 plus grands nombres lus, sous forme négative (pour un tas min simulant un tas max).

# La boucle suivante s'exécutera n fois, c'est-à-dire autant de fois que le nombre donné en entrée.
for i in range(n):
    a = input()          # Lire un nouveau nombre depuis l'entrée, sous forme de chaîne de caractères.
    a = int(a)           # Convertir cette chaîne en entier, car nous allons faire des opérations numériques dessus.

    heappush(h, -a)      # Ajouter (-a) dans la structure "tas" h. On ajoute l'opposé de a pour inverser l'ordre : ainsi, le plus grand a correspondra au "plus petit" -a, facilitant la gestion des plus grands nombres dans un tas min.
    heappop(h)           # Extraire et retirer l'élément le plus petit du tas h (cela maintient toujours la taille du tas à 4) : si on a ajouté un élément plus grand que les plus petits précédents, celui-ci sera conservé.

# Après cette boucle, h contient les 4 plus grands nombres lus, mais sous forme de valeurs négatives.

h = [str(-a) for a in h]  # Transformer chaque élément négatif a du tas en son opposé positif (-a), puis convertir ce nombre entier en chaîne de caractères. 
                          # On obtient ainsi une liste de chaînes représentant les 4 plus grands nombres lus.

ans = []                  # Créer une liste vide appelée ans, qui servira à stocker des nombres obtenus en concaténant les chaînes de h.

# On utilise deux boucles imbriquées pour parcourir toutes les paires possibles (i, j) où i < j parmi les indices 0,1,2,3.
for i in range(3):        # i ira de 0 à 2 inclus
    for j in range(i+1, 4):  # j ira de i+1 à 3 inclus, garantissant que j > i, évitant ainsi les répétitions et l’auto-concaténation.

        ans.append(int(h[i]+h[j]))  # Concaténer la chaîne à l’indice i avec celle à l’indice j, puis convertir ce résultat en entier, et l'ajouter à la liste ans.
        ans.append(int(h[j]+h[i]))  # De même, concaténer dans l’ordre inverse (j puis i), convertir en entier, et ajouter aussi. 
                                     # Cela génère toutes les combinaisons possibles avec deux nombres dans h.

ans.sort()                  # Trier la liste ans dans l’ordre croissant, ce qui organise tous les nombres concaténés du plus petit au plus grand.

print ans[2]                # Afficher (sur la sortie standard) le troisième élément de la liste triée ans. 
                            # Comme l’indexation commence à 0, ans[2] correspond au troisième plus petit nombre concaténé ainsi constitué.