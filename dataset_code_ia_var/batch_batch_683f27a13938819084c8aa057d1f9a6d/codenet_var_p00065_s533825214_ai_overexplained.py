import sys # Importe le module sys qui permet d'accéder à certains objets utilisés par l'interpréteur Python, ici sys.stdin pour la lecture des entrées standard

C = range(1001) # Définit une séquence de nombres entiers allant de 0 à 1000 inclus. Ceci crée un objet range utilisé pour indexer et initialiser une liste à 1001 éléments.

m = 0 # Initialise une variable m à 0. Cette variable va agir comme un indicateur pour choisir la ligne dans la liste d créée ci-dessous.

# Crée une liste de deux sous-listes (donc deux lignes). Chaque sous-liste contient 1001 zéros.
# La compréhension de liste fonctionne comme suit :
#   pour j dans C (c'est-à-dire de 0 à 1000), créer une sous-liste
#   chaque sous-liste consiste en un zéro pour chaque i dans C (donc 1001 zéros)
d = [[0 for i in C] for j in range(2)]

# Lit chaque ligne de l'entrée standard (c-à-d, ce que l'utilisateur tape ou un fichier redirigé)
for s in sys.stdin.readlines(): 
    # Si la ligne est un simple saut de ligne (donc, une ligne complètement vide ou qui ne contient qu'un retour à la ligne)
    if s == "\n":
        m += 1 # Incrémente m de 1. Cela signifie que nous allons maintenant travailler sur la deuxième sous-liste de d (d[1]) pour les futures entrées.
    else:
        # Sinon, la ligne contient des données, supposément sous la forme "a,b"
        # Utilise la fonction split pour diviser la chaîne s sur la virgule et map pour convertir chaque morceau en entier
        a, b = map(int, s.split(','))
        # Incrémente de 1 l'élément à l'index a dans la sous-liste d[m]
        # Cela enregistre une occurrence de l'indice a pour le groupe courant (0 ou 1 selon m)
        d[m][a] += 1

# Pour chaque valeur i dans la plage 0 à 1000
for i in C:
    a = d[0][i] # Récupère le nombre de fois où l'indice i a été vu dans le premier groupe (avant la ligne vide)
    b = d[1][i] # Récupère le nombre de fois où l'indice i a été vu dans le second groupe (après la ligne vide)
    # Si la valeur a ET la valeur b sont non nulles (autrement dit, si i a été vu dans les deux groupes)
    if a and b:
        # Affiche i suivi du total d'occurrences de i dans les deux groupes (a + b)
        # print i, a+b dans Python 2 ; mais en Python 3, il faut utiliser parenthèses
        print(i, a + b)