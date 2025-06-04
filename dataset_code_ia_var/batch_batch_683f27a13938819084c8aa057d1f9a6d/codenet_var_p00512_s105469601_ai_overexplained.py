# Création d'un dictionnaire vide nommé 'data'. Ce dictionnaire sera utilisé pour stocker des associations clé-valeur,
# où les clés sont des chaînes, et les valeurs sont des entiers représentant un cumul.
data = {}

# La fonction 'input()' lit une ligne depuis l'entrée standard (habituellement le clavier).
# Ensuite, 'int(input())' convertit cette chaîne en un entier.
# 'range(int(input()))' crée un objet range allant de 0 jusqu'au nombre spécifié.
# 'for _ in range(int(input())):' itère ce bloc de code autant de fois que l'utilisateur a indiqué,
# '_' est un nom de variable souvent utilisé lorsque la variable de boucle n'est pas utilisée dans le bloc.
for _ in range(int(input())):
    # 'input().split()' lit une ligne de texte, et la découpe en liste de mots (selon les espaces).
    # En écrivant 'p, n = input().split()', la première valeur sera attribuée à 'p', la deuxième à 'n'.
    p, n = input().split()
    
    # La méthode 'get()' du dictionnaire permet d'obtenir la valeur associée à la clé 'p'.
    # Si 'p' n'est pas encore dans 'data', 'data.get(p, 0)' renvoie 0 par défaut.
    # Ensuite, on ajoute 'int(n)' à cette valeur : 'int(n)' convertit la chaîne 'n' en entier.
    # Cette somme est attribuée de nouveau à la clé 'p' dans le dictionnaire 'data'.
    data[p] = data.get(p, 0) + int(n)

# La compréhension de liste suivante : '[[len(a), a] for a in data.keys()]'
# parcourt toutes les clés du dictionnaire avec 'for a in data.keys()', où 'a' est chaque clé (une chaîne).
# Pour chaque clé, elle calcule la longueur de la chaîne (nombre de caractères) avec 'len(a)',
# et crée une liste [longueur, clé]. Le résultat est donc une liste de listes, où chaque sous-liste 
# contient la longueur d'une clé, et la clé elle-même.
# La fonction 'sorted()' trie cette liste de listes en fonction du premier élément de chaque sous-liste,
# c'est-à-dire la longueur des clés. (En cas d'égalité, les clés sont ordonnées alphabétiquement grâce au tri sur le second élément.)
k = sorted([[len(a), a] for a in data.keys()])

# Boucle de parcours de la liste triée 'k'.
# Chaque élément de 'k' est une sous-liste de deux éléments: [longueur, clé].
# La notation 'for _, i in k:' décompose chaque sous-liste en deux variables,
# la première (longueur) attribuée à '_', car elle n'est pas utilisée, 
# et la deuxième, la clé, attribuée à 'i'.
for _, i in k:
    # Affichage de la clé 'i' et de sa valeur associée dans le dictionnaire 'data'.
    # Les deux valeurs sont séparées par un espace par défaut dans la fonction 'print'.
    print(i, data[i])