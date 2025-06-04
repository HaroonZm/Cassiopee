# Prend deux entiers n et k comme entrée utilisateur, séparés par un espace
# split() sépare l'entrée sur l'espace, map() convertit les deux éléments en int
n, k = map(int, input().split())

# Crée une liste 'li' qui va contenir n entiers.
# [int(input()) for i in range(n)] est appelé compréhension de liste.
# Elle exécute la boucle for i in range(n), donc pour chaque i de 0 à n-1, exécute int(input()).
# int(input()) prend un entier au clavier et le convertit de str à int.
li = [int(input()) for i in range(n)]

# Initialise une liste vide appelée 'diff' qui va stocker les différences.
diff = []

# Boucle sur les indices j de 0 à n-2 (car range(n-1) s'arrête à n-2 compris).
for j in range(n-1):
    # Calcule la différence entre l'élément suivant et l'élément courant.
    # li[j+1] est l'élément à l'indice suivant, li[j] est l'élément à l'indice courant.
    # Soustrait 1 à la différence. Par exemple si li[j+1]=8, li[j]=5 :
    # diff = 8 - 5 - 1 = 2.
    diff.append(li[j+1] - li[j] - 1)

# Trie la liste 'diff' en ordre décroissant.
# reverse=True veut dire que le plus grand sera en premier dans la liste.
diff.sort(reverse=True)

# Calcule la somme de tous les éléments de 'diff' de l'indice k-1 jusqu'à la fin de la liste.
# diff[k-1:] est la 'slice' de la liste 'diff' allant de l'indice k-1 jusqu'à la fin.
# sum() ajoute tous les éléments de cette sous-liste.
# Ajoute n à cette somme (correspondant probablement au nombre d’éléments originaux).
# print() affiche ce résultat final à l’écran.
print(n + sum(diff[k-1:]))