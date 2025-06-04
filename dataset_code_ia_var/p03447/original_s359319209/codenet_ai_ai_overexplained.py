# Demander à l'utilisateur de saisir une première valeur, lire l'entrée clavier au format texte (string)
# La fonction input() affiche une invite vide (rien entre les parenthèses) et attend une saisie utilisateur
# int(...) transforme l'entrée saisie en nombre entier (integer)
# La première valeur entière saisie par l'utilisateur est obtenue ici
premiere_valeur = int(input())

# Demander à l'utilisateur de saisir une seconde valeur, même principe que ci-dessus
# Saisie d'un second entier par l'utilisateur
seconde_valeur = int(input())

# Demander à l'utilisateur de saisir une troisième valeur, même principe
# Saisie d'un troisième entier par l'utilisateur
troisieme_valeur = int(input())

# Effectuer la soustraction de la première valeur moins la seconde valeur
# L'opérateur "-" permet de soustraire deux nombres
difference = premiere_valeur - seconde_valeur

# Calculer le modulo, c'est-à-dire le reste de la division euclidienne de 'difference' par 'troisieme_valeur'
# L'opérateur "%" renvoie ce reste
resultat = difference % troisieme_valeur

# Afficher le résultat sur la sortie standard (l'écran)
# print() permet d'afficher une valeur à l'utilisateur
print(resultat)