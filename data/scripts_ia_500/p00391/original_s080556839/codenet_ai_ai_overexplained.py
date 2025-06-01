# Lecture de l'entrée utilisateur : on attend que l'utilisateur entre deux nombres entiers séparés par un espace.
# Ces deux nombres représenteront les variables W et H, probablement des dimensions ou des tailles.
# La fonction input() récupère une chaîne de caractères depuis l'entrée standard.
# La méthode split() divise cette chaîne en une liste de sous-chaînes, utilisant l'espace comme séparateur par défaut.
# map(int, ...) applique la fonction int à chaque élément de la liste créée par split(), ce qui convertit chaque chaîne en entier.
# Enfin, on assigne ces deux entiers directement à W et H grâce au déballage (unpacking).
W, H = map(int, input().split())

# Lecture de la liste A à partir d'une ligne d'entrée suivante. 
# De nouveau, input() lit une chaîne, split() divise cette chaîne en composants, et map(int, ...) convertit chacun en entier.
# Les entiers sont ensuite transformés en liste grâce à l'opérateur * (extraction) placé devant la variable A entre crochets,
# ce qui permet de créer une nouvelle liste contenant tous les éléments renvoyés par map.
# Cela est équivalent à écrire A = list(map(int, input().split())), ici l'utilisation de * crée une liste à partir d’un itérable.
*A, = map(int, input().split())

# Même opération qu'au-dessus pour lire la liste B.
*B, = map(int, input().split())

# Tri de la liste A en ordre décroissant (du plus grand au plus petit).
# La méthode sort() modifie la liste A en place.
# L'argument reverse=1 (equivalent à reverse=True) signifie que l'on inverse l'ordre naturel (croissant) pour obtenir un tri décroissant.
A.sort(reverse=1)

# Initialisation de la variable 'ok'.
# La syntaxe 'ok =+ (sum(A) == sum(B))' semble être une erreur.
# En Python, '=+' n'est pas un opérateur valide. Il s'agit surement d'une faute de frappe pour 'ok = +(...)' ou 'ok += ...'.
# Ici, supposons qu'on voulait initialiser ok à 1 si la somme des éléments de A égale la somme des éléments de B, sinon 0.
# sum(A) calcule la somme des éléments de la liste A.
# sum(B) de même pour B.
# L'expression (sum(A) == sum(B)) retourne un booléen True ou False.
# En Python, True est équivalent à 1 et False à 0 lorsqu'on effectue des opérations arithmétiques.
# L'opérateur unaire + convertit explicitement True/False en entier 1/0.
ok = + (sum(A) == sum(B))

# Boucle sur chaque élément 'a' de la liste A.
for a in A:
    # À chaque passage de la boucle extérieure, on trie la liste B en ordre décroissant comme pour A.
    B.sort(reverse=1)
    
    # Boucle de 0 à a-1, c'est-à-dire on répète 'a' fois les opérations suivantes.
    # Cette boucle permettra d'essayer de soustraire 1 d'autant d'éléments en tête de liste B.
    for i in range(a):
        # On vérifie ici deux conditions de sortie:
        # 1) Si l'index i dépasse la longueur de B, cela signifie qu'il n'y a pas assez d'éléments dans B pour satisfaire la demande.
        # 2) Si l'élément B[i] est 0, cela signifie qu'on ne peut plus soustraire 1, car ce nombre est à zéro.
        # Dans ces deux cas, on met ok à 0 pour indiquer l'échec, et on sort de la boucle intérieure par break.
        if i >= len(B) or B[i] == 0:
            ok = 0
            break
        
        # Sinon, si la condition précédente n'est pas vraie, on décrémente la valeur de B[i] de 1.
        # Cela signifie qu'on "consume" ou on retire une unité de la valeur stockée dans B[i].
        B[i] -= 1

# Enfin, on affiche la valeur de la variable ok.
# Ok vaudra 1 si aucune des conditions d'échec n'a été rencontrée,
# c'est-à-dire que la somme de A et B étaient égales et que chaque élément de A a pu "réduire" les éléments correspondants de B.
# Sinon, ok vaudra 0.
print(ok)