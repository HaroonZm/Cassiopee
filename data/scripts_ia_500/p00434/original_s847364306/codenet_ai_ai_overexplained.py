import math  # Importation du module math, qui contient des fonctions mathématiques avancées. Ici, il n'est pas utilisé mais reste importé, possiblement pour une utilisation future.

# Création d'une liste nommée A contenant les entiers de 1 à 30 inclus.
# La construction est une comprehension list, très utilisée en Python pour créer des listes de manière concise.
# La fonction range(30) génère une séquence d'entiers de 0 à 29.
# Pour chaque entier i dans cette séquence, on ajoute 1, ce qui donne des nombres de 1 à 30.
A = [i+1 for i in range(30)]

# Création d'une seconde liste nommée B composée des 28 entiers entrés par l'utilisateur.
# La comprehension liste itère 28 fois (de 0 à 27) et à chaque itération,
# elle appelle la fonction input() qui affiche une invite permettant à l'utilisateur de saisir une valeur.
# La valeur saisie est de type chaîne (string) initialement, donc on la convertit en entier avec int().
B = [int(input()) for i in range(28)]

# Calcul de la différence entre les ensembles A et B.
# set(A) crée un objet ensemble (set) contenant les éléments uniques de la liste A.
# set(B) fait de même pour la liste B.
# L'opération set(A)-set(B) retourne un nouvel ensemble contenant les éléments présents dans A mais absents dans B.
# On transforme ensuite cet ensemble en liste avec list() afin de pouvoir trier et indexer ces éléments.
# La fonction sorted() trie cette liste par ordre croissant.
diff = sorted(list(set(A) - set(B)))

# Affichage du premier élément de la liste diff. 
# En Python, les indices commencent à 0, donc diff[0] correspond au premier élément.
print(diff[0])

# Affichage du second élément de la liste diff.
# diff[1] correspond au deuxième élément dans la liste diff.
print(diff[1])