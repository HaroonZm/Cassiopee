# Demande à l'utilisateur de saisir une entrée et affecte la valeur saisie à la variable I.
# La fonction input() lit une ligne de texte depuis la console (ou terminal utilisateur).
I = input()

# La fonction len() retourne la longueur (c'est-à-dire le nombre de caractères) de la chaîne de caractères stockée dans I.
# Si la longueur de la chaîne I est exactement égale à 2, le bloc suivant sera exécuté.
if len(I) == 2:
    # Affiche la chaîne I telle quelle, sans modification.
    # La fonction print() affiche la valeur passée en argument sur la sortie standard.
    print(I)
else:
    # Si la longueur de I N'EST PAS 2 (donc peut-être 3 ou une autre valeur),
    # cette partie du code va s'exécuter.
    
    # On accède alors à des caractères individuels dans I en utilisant l'opérateur d'indexation [] :
    # I[2] signifie le 3ème caractère de la chaîne I (les indices commencent à 0 en Python)
    # I[1] est le 2ème caractère
    # I[0] est le 1er caractère
    # On les concatène avec l'opérateur +, qui enchaîne les chaînes les unes à la suite des autres.
    
    # Puis on affiche ce nouveau résultat.
    print(I[2] + I[1] + I[0])