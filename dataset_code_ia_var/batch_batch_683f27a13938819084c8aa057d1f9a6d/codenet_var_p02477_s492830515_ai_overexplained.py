import sys  # Importe le module 'sys' qui permet d'interagir avec certains aspects du système d'exploitation, notamment les entrées/sorties standard

# Utilise la fonction 'readline' du module 'sys.stdin' pour lire une ligne depuis l'entrée standard (par exemple, ce que l'utilisateur tape au clavier)
# Cela permet d'obtenir toutes les données saisies en une seule ligne sous forme de chaîne de caractères (string)
ligne = sys.stdin.readline()

# Utilise la méthode 'split()' sur la chaîne lue pour séparer la ligne en une liste de sous-chaînes (listes de mots ici), en prenant comme séparateur l'espace par défaut
# Cela découpe la chaîne selon les espaces, permettant d'obtenir chaque valeur saisie séparément (ex : "3 4" devient ["3", "4"])
morceaux = ligne.split()

# Utilise la fonction 'map' pour appliquer la conversion 'int' à chaque élément de la liste obtenue précédemment. 
# Cela permet de transformer les sous-chaînes de caractères représentant des entiers en véritables entiers (par exemple, "3" devient 3)
# Le résultat de 'map' n'est pas une liste mais un itérable; on l'utilise ici pour unpacker dans deux variables
a, b = map(int, morceaux)  # 'a' reçoit la première valeur, 'b' la seconde (les deux sont convertis en entiers)

# Calcule le produit des deux variables entières obtenues lors de l'étape précédente (c'est-à-dire la multiplication de 'a' par 'b')
resultat = a * b  # Utilise l'opérateur '*' qui fait la multiplication en Python

# Affiche le résultat calculé à l'écran en utilisant la fonction intégrée 'print'
# 'print' affiche dans la sortie standard (typiquement l'écran de l'utilisateur)
print(resultat)