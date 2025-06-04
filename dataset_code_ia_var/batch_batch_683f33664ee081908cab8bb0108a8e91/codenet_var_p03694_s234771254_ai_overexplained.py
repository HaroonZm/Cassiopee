#!/usr/bin/env python3

# Demande à l'utilisateur d'entrer une valeur depuis le clavier (au format texte/chaîne de caractères)
# La fonction input() lit la saisie de l'utilisateur jusqu'à ce qu'il appuie sur Entrée.
# La fonction int() convertit cette chaîne de caractères en un entier (nombre sans décimale).
N = int(input())

# Demande à l'utilisateur de saisir plusieurs nombres séparés par des espaces, sur une seule ligne.
# La fonction input() lit cette ligne complète de texte.
# La fonction split() sans argument divise la chaîne sur les espaces et crée une liste de chaînes de caractères,
# chaque chaîne représentant un nombre.
# La fonction map() applique la fonction int à chaque élément de cette liste, transformant chaque chaîne
# en entier correspondant.
# La fonction list() convertit l'objet résultant de map (qui est un itérable) en une liste réelle de valeurs entières.
a = list(map(int, input().split()))

# La fonction sorted() prend cette liste d'entiers et retourne une nouvelle liste où les éléments sont
# triés dans l'ordre croissant (du plus petit au plus grand).
a = sorted(a)

# Pour obtenir l'écart entre la plus grande valeur et la plus petite valeur de la liste a :
# a[0] fait référence au tout premier élément de la liste a, qui est, grâce au tri, le plus petit nombre.
# a[-1] fait référence au dernier élément de la liste a, qui est, grâce au tri, le plus grand nombre.
# On soustrait donc le plus petit nombre de la liste du plus grand pour obtenir la différence maximale entre
# les éléments de la liste.
# Enfin, on affiche le résultat à l'écran en utilisant la fonction print(), qui convertit le résultat en chaîne de caractères.
print(a[-1] - a[0])