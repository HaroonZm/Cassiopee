# Demande à l'utilisateur de saisir une entrée au clavier en utilisant la fonction input()
# L'entrée reçue est toujours une chaîne de caractères (str) par défaut
# Pour pouvoir comparer des nombres, on convertit la chaîne de caractères en entier (int) avec la fonction int()
# On stocke cette valeur entière dans la variable nommée 'n'
n = int(input())

# On commence une structure conditionnelle pour vérifier la valeur de 'n'
# Le mot-clé 'if' permet de tester une condition
# Ici, on vérifie si la valeur contenue dans 'n' est exactement égale (==) à 25
if n == 25:
    # Si la condition précédente est vraie (n vaut 25), alors la fonction print() affichera "Christmas"
    print("Christmas")
# 'elif' signifie 'else if', c'est-à-dire 'sinon, si la condition suivante est vraie'
# On vérifie ici si 'n' est égal à 24
elif n == 24:
    # Si n vaut 24, la fonction print() affichera "Christmas Eve"
    print("Christmas Eve")
# On vérifie une autre condition si toutes les précédentes sont fausses : est-ce que 'n' est égal à 23 ?
elif n == 23:
    # Si n vaut 23, alors on affiche "Christmas Eve Eve"
    print("Christmas Eve Eve")
# L'instruction 'else' permet d'exécuter un bloc si aucune des conditions précédentes n'est vraie
else:
    # Ici, si 'n' est différent de 25, 24 et 23, alors on affiche "Christmas Eve Eve Eve"
    print("Christmas Eve Eve Eve")