# Demande à l'utilisateur de saisir deux entiers séparés par un espace, qui seront assignés à N et L
# La fonction input() lit une ligne entrée au clavier sous forme de chaîne de caractères
# La méthode split() coupe la chaîne en morceaux autour des espaces et crée une liste de sous-chaînes
# La fonction map(int, ...) applique int() à chaque élément de la liste, les transformant en entiers
# Les deux valeurs entières sont ensuite affectées à N et L
N, L = map(int, input().split())

# Déclare une liste vide appelée apple, qui va stocker les valeurs des pommes
apple = []

# Utilise une boucle for pour créer des nombres allant de L à L+N-1 inclus
# La variable i commence à 0 et s'incrémente jusqu'à N-1
for i in range(N):
    # À chaque itération, ajoute (L + i) à la liste apple
    # Cela correspond à la saveur de chaque pomme située consécutivement à partir de L
    apple.append(L + i)

# Trie la liste apple avec la méthode sort()
# Le paramètre key=abs indique qu'on veut trier la liste selon la valeur absolue de chaque élément
# Cela veut dire que les éléments les plus proches de 0 viendront au début de la liste
apple.sort(key=abs)

# Supprime le premier élément de la liste apple avec la notation [1:]
# Cela crée une nouvelle liste qui commence à l'indice 1 et va jusqu'à la fin de la liste
# Le premier élément, c'est-à-dire celui avec la plus petite valeur absolue, est ainsi retiré
apple = apple[1:]

# Utilise la fonction sum() pour additionner tous les éléments restants dans la liste apple
# Le résultat, qui représente la somme des saveurs après avoir retiré la pomme la plus neutre, est affecté à ans
ans = sum(apple)

# Affiche la valeur calculée de ans à l'écran
print(ans)