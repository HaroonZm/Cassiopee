# Demande à l'utilisateur d'entrer une valeur entière via le clavier.
# La fonction input() lit une ligne depuis l'entrée standard (le clavier), qui est toujours renvoyée sous forme de chaîne de caractères.
# La fonction int() convertit cette chaîne de caractères en un nombre entier (type int).
n = int(input())

# Demande à l'utilisateur d'entrer une chaîne de caractères via le clavier.
# La fonction input() lit également une ligne depuis l'entrée standard.
s = input()

# La méthode find() est utilisée sur la chaîne de caractères s.
# s.find('>') retourne l'index de la première occurrence du caractère '>' dans s.
# Si '>' n'est pas trouvé, find() retourne -1.
premier_index_chevron_droite = s.find('>')

# La méthode rfind() est utilisée sur la chaîne de caractères s.
# s.rfind('<') retourne l'index de la dernière occurrence du caractère '<' dans s.
# Si '<' n'est pas trouvé, rfind() retourne -1.
dernier_index_chevron_gauche = s.rfind('<')

# Calcul du nombre d'éléments à droite du dernier '<' :
# n est la longueur totale de la chaîne (ou l'entier saisi initialement).
# dernier_index_chevron_gauche + 1 est la position de l'élément juste après le dernier '<'.
# n - (dernier_index_chevron_gauche + 1) donne le nombre de caractères après le dernier '<'.
nb_caracteres_apres_dernier_chevron_gauche = n - dernier_index_chevron_gauche - 1

# La fonction min() retourne la plus petite valeur parmi les deux calculées ci-dessus :
# - l'index du premier '>' trouvé (premier_index_chevron_droite)
# - le nombre de caractères après le dernier '<' (nb_caracteres_apres_dernier_chevron_gauche)
min_valeur = min(premier_index_chevron_droite, nb_caracteres_apres_dernier_chevron_gauche)

# Calcul final :
# Soustrait la plus petite des deux valeurs précédentes de n afin d'obtenir le résultat.
# Puis cette valeur est affichée sur la console grâce à la fonction print().
print(n - min_valeur)