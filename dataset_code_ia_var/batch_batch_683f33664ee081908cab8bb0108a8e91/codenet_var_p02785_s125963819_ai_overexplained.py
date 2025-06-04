# Lecture de deux entiers à partir de l'entrée standard (habituellement le clavier)
# La fonction input() lit une ligne de texte sous forme de chaîne de caractères
# split() divise cette chaîne en une liste de sous-chaînes, en séparant là où il y a des espaces
# map(int, ...) applique la fonction int à chaque sous-chaîne pour obtenir une liste d'entiers
# La fonction map() retourne un itérable ; l'utilisation de la syntaxe 'N, K = ...' affecte les deux premiers éléments du résultat à N et K
N, K = map(int, input().split())

# Lire une autre ligne d'entrée utilisateur contenant des entiers séparés par des espaces
# map(int, ...) convertit chaque chaîne en entier, créant un itérable d'entiers
# list(...) convertit cet itérable en une liste Python stockée dans la variable H
H = list(map(int, input().split()))

# Trier la liste H par ordre décroissant (du plus grand au plus petit)
# La méthode sort() modifie la liste en place
# reverse=True indique que le tri doit être fait en ordre inverse (décroissant)
H.sort(reverse=True)

# Exclure (enlever) les K premiers éléments de la liste H
# L'opération de découpage H[K:] prend tous les éléments de H à partir de l'indice K (en incluant K, car l'indice commence à zéro),
# c'est-à-dire qu'elle ignore les K premiers éléments les plus grands grâce au tri précédent
# Le résultat du découpage est réaffecté à H lui-même (H prend une nouvelle valeur qui est la liste tronquée)
H = H[K:]

# Calculer la somme totale de tous les éléments de la liste H (c'est-à-dire la somme des entiers restants après découpage)
# sum(H) retourne la somme des valeurs de la liste H
# print(...) affiche le résultat calculé (la somme) à la sortie standard (habituellement l'écran)
print(sum(H))