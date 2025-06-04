# Demande à l'utilisateur de saisir une ligne d'entrée au clavier
# La fonction input() attend que l'utilisateur tape quelque chose puis appuie sur 'Entrée'
# Le texte saisi est récupéré sous forme de chaîne de caractères (string)
# Par exemple, si l'utilisateur tape: 1 2 3
# input() retournera la chaîne "1 2 3"
saisie_utilisateur = input()

# La méthode split() sépare la chaîne de caractères selon les espaces blancs par défaut
# Elle retourne une liste de sous-chaînes, chaque sous-chaîne correspondant à un nombre saisi
# Exemple: "1 2 3".split() donnera ['1', '2', '3']
liste_de_chaines = saisie_utilisateur.split()

# La fonction map() permet d'appliquer une fonction à chaque élément d'un itérable (comme une liste)
# Ici, map(int, liste_de_chaines) transforme chaque élément de la liste (qui sont des chaînes) en entiers
# Ceci revient à faire [int(elt) for elt in liste_de_chaines], mais map() est généralement plus compact
iterateur_integers = map(int, liste_de_chaines)

# La fonction list() convertit l'itérateur retourné par map() en une liste réelle stockée en mémoire
# Au final, x contiendra une liste d'entiers correspondant aux valeurs saisies par l'utilisateur
# Exemple: Si l'utilisateur a tapé "1 2 3", alors x vaudra [1, 2, 3]
x = list(iterateur_integers)

# La fonction sum() additionne tous les éléments présents dans l'itérable passé en argument
# Ici, sum(x) va calculer la somme des entiers dans la liste x
# Exemple: Si x = [1, 2, 3], alors sum(x) retournera 6
somme_des_x = sum(x)

# Le nombre 15 est une constante utilisée dans ce programme
# On fait la soustraction : 15 moins la somme des entiers saisis par l'utilisateur
# Cette valeur représente le résultat final que l'on veut afficher
resultat = 15 - somme_des_x

# La fonction print() affiche la valeur du paramètre passé à la sortie standard (l'écran)
# Ici, on affiche le résultat de l'opération précédente
print(resultat)