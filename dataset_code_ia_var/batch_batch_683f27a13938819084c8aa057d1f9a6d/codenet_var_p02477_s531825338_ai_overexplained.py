# Demande à l'utilisateur de saisir une ligne de texte, en général depuis le clavier.
# La fonction input() attend que l'utilisateur saisisse une donnée puis appuie sur 'Entrée'.
# Le texte saisi est récupéré sous forme de chaîne de caractères (str).
ligne = input()

# La méthode split() coupe la chaîne de caractères 'ligne' en une liste de sous-chaînes,
# en utilisant comme séparateur l'espace par défaut. Par exemple, si l'utilisateur saisit
# "5 9", split() produira la liste ["5", "9"].
morceaux = ligne.split()

# La fonction map() applique une fonction, ici la fonction int(), à chaque élément de la liste 'morceaux'.
# int() convertit les chaînes de caractères représentant des chiffres ("5", "9") en entiers (5, 9).
# map(int, morceaux) produit donc un itérable de deux entiers : 5 et 9 (dans cet exemple).
# On utilise ensuite un "unpacking" (dépaquetage) avec A, B = ... pour affecter respectivement le premier et le second
# entier de l'itérable aux variables nommées A et B.
A, B = map(int, morceaux)

# On effectue ensuite une multiplication des deux entiers obtenus, A et B.
# L'opérateur * réalise la multiplication. Si A vaut 5 et B vaut 9, le résultat sera 45.

# La fonction print() affiche ce résultat à l'écran, en le convertissant en chaîne de caractères si nécessaire.
# print() ajoute automatiquement un retour à la ligne à la fin de l'affichage.
print(A * B)