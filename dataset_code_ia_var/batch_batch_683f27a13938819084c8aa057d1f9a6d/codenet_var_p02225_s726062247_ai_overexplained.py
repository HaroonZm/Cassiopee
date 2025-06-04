# Demander à l'utilisateur de saisir une valeur
# La fonction input() attend que l'utilisateur saisisse quelque chose sur le clavier et valide avec Entrée
# Le résultat de input() est toujours une chaîne de caractères (type str)
# La fonction int() prend cette chaîne et la convertit en entier (type int)
# On stocke ce nombre entier dans la variable 'n'
n = int(input())  # Exemple : si l'utilisateur tape '3', alors n vaudra 3

# Demander à l'utilisateur de saisir une liste de nombres, séparés par des espaces
# Encore une fois, input() renvoie la saisie sous forme de chaîne de caractères
# On utilise split() qui sépare la chaîne là où il y a des espaces et retourne une liste de sous-chaînes
# Par exemple, si l'utilisateur tape '1 2 3', split() renverra ['1', '2', '3']
# map() applique ici la fonction int à chaque élément de la liste, transformant chaque sous-chaîne en un entier
# map(int, ...) produit donc un objet map contenant des entiers
# sum() accepte cet objet, additionne tous les éléments et renvoie la somme totale
# print() affiche le résultat à l'écran
print(sum(map(int, input().split())))  # Si l'utilisateur tape '1 2 3', alors print affichera 6