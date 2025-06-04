from sys import stdin  # Importation du module sys et accès à l'objet stdin pour la lecture des entrées standard

# Lecture d'une ligne à partir de l'entrée standard (l'utilisateur tape une ligne puis appuie sur Entrée)
ligne = stdin.readline()  # La méthode readline() lit une ligne jusqu'au saut de ligne (\n), y compris le caractère de fin de ligne

# Suppression des espaces blancs et des caractères de nouvelle ligne à la fin de la chaîne lue
ligne_sans_espaces = ligne.rstrip()  # rstrip() retourne une nouvelle chaîne avec les espaces à droite supprimés

# Conversion de la chaîne de caractères en une liste de caractères individuels :
# Exemple : '101' -> ['1', '0', '1']
liste_caracteres = list(ligne_sans_espaces)

# Utilisation de la fonction map pour convertir chaque caractère de la liste en entier (int) :
# map(int, liste_caracteres) applique int() sur chaque élément
# list(...) permet de reconvertir le résultat de map en liste d'entiers
s = list(map(int, liste_caracteres))

# Comptage du nombre d'occurrences de la valeur 1 dans la liste s avec s.count(1)
nombre_de_un = s.count(1)

# Comptage du nombre d'occurrences de la valeur 0 dans la liste s avec s.count(0)
nombre_de_zero = s.count(0)

# Calcul du minimum entre le nombre de 1 et de 0 :
# min(nombre_de_un, nombre_de_zero) retourne la plus petite des deux valeurs
minimum_de_un_et_zero = min(nombre_de_un, nombre_de_zero)

# Multiplication du minimum trouvé par 2 :
# Ceci donne le double du nombre le plus faible entre 0 et 1 présents dans la liste
resultat_final = minimum_de_un_et_zero * 2

# Affichage du résultat final obtenu avec la fonction print :
# Ceci affiche le résultat sur une ligne à la sortie standard (habituellement la console)
print(resultat_final)