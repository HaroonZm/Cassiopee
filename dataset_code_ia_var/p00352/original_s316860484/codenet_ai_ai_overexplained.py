# Demander à l'utilisateur de saisir deux nombres entiers séparés par un espace
# La fonction input() affiche une invite à l'utilisateur et attend qu'il saisisse une ligne de texte au clavier
# Par exemple, l'utilisateur peut entrer : 5 7

input_line = input()  # Stocke la chaîne de caractères saisie par l'utilisateur dans la variable input_line

# Utiliser la méthode split() sur la chaîne de caractères
# split() sépare la chaîne en une liste de sous-chaînes (morceaux) en utilisant l'espace comme séparateur par défaut
# Par exemple, si input_line vaut "5 7", input_line.split() renvoie ["5", "7"]
split_values = input_line.split()

# La fonction map() permet d'appliquer une fonction à chaque élément d'un itérable (ici, la liste split_values)
# Ici, on applique la fonction int (convertion en entier) à chaque sous-chaîne pour obtenir des entiers à la place de chaînes
# Cela donne un objet map contenant tous les entiers convertis

mapped_integers = map(int, split_values)

# On utilise l'affectation multiple (décomposition) pour stocker les deux valeurs obtenues dans les variables a et b
# Cela suppose que split_values contenait exactement deux éléments, soit deux nombres saisis par l'utilisateur
a, b = mapped_integers  # a contiendra le premier entier, b le second

# Additionner les deux nombres a et b
somme = a + b  # On effectue l'addition et stocke le résultat dans la variable somme

# Utiliser l'opérateur // pour effectuer une division entière
# La division entière (//) donne le quotient de la division sans la partie décimale
# Par exemple, (5+7)//2 = 12//2 = 6
moyenne_entiere = somme // 2  # On stocke le résultat de la division entière dans la variable moyenne_entiere

# Afficher la moyenne entière obtenue à l'écran
# print() affiche le contenu spécifié dans la console
print(moyenne_entiere)  # Affiche le résultat final