# On commence par récupérer une ligne d'entrée utilisateur, c'est-à-dire ce que l'utilisateur tape au clavier suivi de la touche Entrée.
# La fonction input() attend que l'utilisateur saisisse une chaîne de caractères et appuie sur Entrée.
# Ensuite, on utilise la méthode split() sur cette chaîne pour diviser la chaîne en une liste de sous-chaînes,
# en séparant la chaîne originale à chaque espace trouvé.
# Par exemple, si l'utilisateur tape "1 4 2 3", split() retournera la liste ["1", "4", "2", "3"].
# Après cela, on applique la fonction map() pour convertir chaque élément de la liste de chaînes en un entier.
# map(int, liste) prend chaque élément de la liste et applique la fonction int() pour convertir la chaîne en nombre entier.
# Le résultat de map est un itérateur d'entiers et on le convertit en liste pour pouvoir y accéder par indices,
# mais ici la conversion vers liste n'est pas explicite car on utilise directement sorted().
# La fonction sorted() prend cette séquence d'entiers et retourne une nouvelle liste où ces entiers sont triés dans l'ordre croissant.
# Ainsi, lst est une liste triée d'entiers fournis par l'utilisateur.
lst = sorted(map(int, input().split()))

# Maintenant, on vérifie une condition composée de trois parties.
# Cette condition compare des éléments spécifiques dans la liste lst.
# lst[0] est le premier élément de la liste (car les indices commencent à 0 en Python).
# lst[3] est le quatrième élément.
# En vérifiant lst[0] == lst[3], on s'assure que le premier élément est égal au quatrième élément.
# De même, lst[4] == lst[7] vérifie que le cinquième élément est égal au huitième,
# et lst[8] == lst[11] vérifie que le neuvième élément est égal au douzième.
# L'opérateur "and" signifie que toutes les trois conditions doivent être vraies pour que l'ensemble soit vrai.
if lst[0] == lst[3] and lst[4] == lst[7] and lst[8] == lst[11]:
    # Si la condition est vraie, on affiche la chaîne de caractères "yes".
    # La fonction print() en Python sert à afficher du texte ou d'autres objets dans la console.
    print("yes")
else:
    # Sinon, si la condition est fausse, on affiche la chaîne "no".
    print("no")