# Importation du module sys afin d'accéder à stdin (entrée standard)
from sys import stdin

# Lecture d'une ligne depuis l'entrée standard.
# stdin.readline() lit toute la ligne (y compris le caractère de retour à la ligne '\n' en fin)
# La méthode rstrip() est utilisée ici pour retirer tout caractère d'espacement à la fin de la chaîne (notamment '\n')
s = stdin.readline().rstrip()

# Définition d'une chaîne de caractères k qui contient la valeur "CODEFESTIVAL2016"
# Cette chaîne représentera la chaîne de référence à laquelle nous allons comparer la chaîne d'entrée s
k = "CODEFESTIVAL2016"

# Initialisation d'un compteur nommé point, qui servira à comptabiliser le nombre de différences (mismatches) entre s et k
# Ce compteur est initialisé à zéro car au début aucune différence n'a encore été trouvée
point = 0

# Boucle for utilisant la fonction range() 
# range(len(s)) va générer une séquence d'entiers démarrant à 0 jusqu'à len(s)-1 inclus
# len(s) donne la longueur de la chaîne de caractères s
# On suppose ici que len(s) et len(k) sont identiques, correspondant à la longueur de "CODEFESTIVAL2016"
for i in range(len(s)):
    # Instruction conditionnelle if
    # On compare ici le i-ème caractère de k (k[i]) avec le i-ème caractère d'entrée s (s[i])
    # Si ces caractères ne sont pas identiques (opérateur !=), alors il y a une différence à cet index
    if k[i] != s[i]:
        # On incrémente alors le compteur point de 1, pour signaler qu'une nouvelle différence a été trouvée
        point += 1

# Après avoir parcouru tous les caractères, on affiche (imprime) la valeur finale de point
# Cela correspond au nombre total de positions où s diffère de k
print(point)