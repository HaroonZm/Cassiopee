# Demander à l'utilisateur de saisir une chaîne de caractères au clavier via la fonction input().
# Par défaut, input() arrête la saisie lorsque l'utilisateur appuie sur 'Entrée'.
# Le texte saisi est récupéré sous forme de chaîne de caractères, c'est-à-dire de type 'str'.
# Ensuite, on utilise la méthode split() sur cette chaîne pour la découper en une liste de segments,
# chaque segment correspondant à un mot séparé par des espaces (par défaut split() utilise l'espace comme séparateur).
# L'opération 'a, b, c = input().split()' réalise en une ligne la lecture, le découpage, et l'affectation :
# Le mot à l'indice 0 de la liste est affecté à 'a', le deuxième à 'b', le troisième à 'c'.

a, b, c = input().split()

# Chacun des mots saisis ('a', 'b', 'c') est une chaîne de caractères.
# Pour obtenir la première lettre de chaque mot, on accède à l'indice [0] de chaque chaîne.
# Exemple : si 'a' vaut "toto", alors a[0] vaut "t".
# Pour transformer cette lettre en majuscule (uppercase), on utilise la méthode upper(),
# qui retourne la chaîne d'origine convertie en majuscule (s'il s'agit d'une lettre).
# On concatène ensuite chacune des lettres majuscules obtenues.
# La fonction print() affiche à l'écran ce qu'on lui passe en argument.
# Ici, on utilise 'sep=""' pour définir le séparateur des éléments imprimés à une chaîne vide,
# c'est-à-dire qu'aucun espace, ni caractère de séparation, ne sera inséré entre les arguments.
# Par défaut, print() utilise un espace comme séparateur, ici on l'empêche.

print(a[0].upper(), b[0].upper(), c[0].upper(), sep="")