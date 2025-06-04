# Demande à l'utilisateur de saisir un entier, qui représentera le nombre d'itérations à effectuer
# input() permet à l'utilisateur de fournir une entrée depuis le clavier en tant que chaîne de caractères
# int() convertit cette chaîne de caractères en un entier qui sera stocké dans la variable n
n = int(input())

# Utilisation d'une boucle for pour répéter un bloc de code un certain nombre de fois
# range(n) génère une séquence de nombres allant de 0 à n-1
# i prend tour à tour chaque valeur de cette séquence, de 0 à n-1 inclus
for i in range(n):
    # Demande à l'utilisateur de saisir un entier pour la première valeur, appelée a
    # input() récupère la saisie utilisateur comme une chaîne de caractères
    # int() convertit cette chaîne de caractères en un entier
    a = int(input())
    
    # Demande à l'utilisateur de saisir un entier pour la deuxième valeur, appelée b
    # input() récupère la saisie utilisateur comme une chaîne de caractères
    # int() convertit cette chaîne de caractères en un entier
    b = int(input())
    
    # Additionne les deux entiers saisis par l'utilisateur et stocke le résultat dans la variable c
    # Ici, c représentera la somme de a et b
    c = a + b
    
    # Convertit le résultat de la somme (c) en une chaîne de caractères afin de pouvoir mesurer sa longueur
    # str() transforme l'entier c en chaîne de caractères
    c = str(c)
    
    # Vérifie si la longueur de la chaîne de caractères représentant la somme est supérieure à 80 caractères
    # len(c) retourne le nombre de caractères dans la chaîne c
    # Si le résultat dépasse 80, cela signifie que la somme est un très grand nombre
    if len(c) > 80:
        # Si la condition précédente est vraie (la longueur est supérieure à 80), affiche le mot "overflow"
        # print() affiche un message à l'écran
        print("overflow")
    else:
        # Si la condition précédente est fausse (la longueur est inférieure ou égale à 80)
        # Affiche la valeur de c, qui est la somme des deux nombres sous forme de chaîne de caractères
        print(c)