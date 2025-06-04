# Demande à l'utilisateur d'entrer une valeur et la stocke dans la variable 'n'.
# La fonction 'input()' renvoie une chaîne de caractères, il faut donc la convertir en entier avec 'int()'.
n = input()              # Lit une ligne depuis l'entrée standard (typiquement le clavier) ; renvoie une chaîne de caractères.
n = int(n)               # Convertit la chaîne de caractères en entier car 'range()' attend un entier comme argument.

# Boucle for : effectue une itération pour chaque valeur de 'k' entre 0 (inclus) et 'n' (exclu).
# La fonction 'range(n)' génère une séquence de nombres de 0 à n-1.
for k in range(n):
    # À chaque itération, deux valeurs sont demandées à l'utilisateur.
    # Première valeur 'a' saisie par l'utilisateur via 'input()' ; stockée comme une chaîne de caractères.
    a = input()

    # Deuxième valeur 'b' saisie par l'utilisateur via 'input()', également stockée comme chaîne.
    b = input()

    # Addition des deux valeurs. Cependant, comme 'a' et 'b' sont des chaînes,
    # il est nécessaire de les convertir en entiers avec 'int()' avant d'effectuer l'opération arithmétique.
    # La variable 'c' va donc contenir la somme numérique des deux entrées.
    c = int(a) + int(b)

    # Conversion de la somme 'c' (de type entier) en chaîne de caractères à l'aide de 'str(c)'.
    # On utilise ensuite 'len()' pour connaître la longueur (nombre de caractères) de cette chaîne.
    # Cela permet de vérifier si le nombre affichable prend plus de 80 caractères.
    if len(str(c)) > 80:
        # Si la somme convertie en chaîne a plus de 80 caractères,
        # on considère qu'il y a un dépassement de capacité et on assigne la chaîne de caractères "overflow" à 'c'.
        c = "overflow"

    # Affiche la valeur de 'c' (qui peut être un entier ou la chaîne "overflow") dans la sortie standard.
    # La syntaxe 'print c' imprime la valeur sur une nouvelle ligne.
    print c