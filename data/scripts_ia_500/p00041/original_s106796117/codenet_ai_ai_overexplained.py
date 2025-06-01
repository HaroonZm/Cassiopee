from itertools import permutations

# Démarrer une boucle infinie, qui continuera à s'exécuter jusqu'à ce qu'on la rompe volontairement avec un break.
while(1):
    # Lire une ligne d'entrée utilisateur, la diviser en éléments séparés par des espaces,
    # et convertir chacun de ces éléments en un entier.
    # Ceci crée une liste d'entiers appelée 'a_'.
    a_ = [int(i) for i in input().split()]

    # Vérifier si la liste entrée est exactement [0, 0, 0, 0].
    # Ce sera la condition d'arrêt pour la boucle infinie.
    if a_ == [0,0,0,0]:
        # Sortir de la boucle infinie si la condition est satisfaite.
        break

    # Générer toutes les permutations possibles des éléments dans la liste 'a_'.
    # 'permutations(a_)' retourne un itérable, on le convertit en liste.
    # Chaque permutation est aussi convertie en liste pour pouvoir accéder par index, 
    # donc on obtient une liste de listes.
    p = list(list(i) for i in permutations(a_))

    # Initialisation d'un flag (drapeau) pour contrôler l'arrêt des boucles imbriquées.
    # Ici, cont = 1 signifie que l'on n'a pas encore trouvé de combinaison qui fonctionne.
    cont = 1

    # Parcours de chaque permutation de quatre éléments, destructurés en variables a, b, c, d.
    for a,b,c,d in p:
        # Si une solution a été trouvée (cont == 0), on arrête la boucle pour ne pas chercher d'autres résultats.
        if cont == 0:
            break

        # Pour chacun des trois opérateurs possible, on fait une boucle.
        # Ces opérations sont les opérations binaires +, -, et *.
        for i in ("+","-","*"):
            if cont == 0:
                break
            for j in ("+","-","*"):
                if cont == 0:
                    break
                for k in ("+","-","*"):       
                    if cont == 0:
                        break

                    # On va essayer différentes combinaisons de parenthèses pour les opérations,
                    # en utilisant exec pour évaluer dynamiquement les expressions.
                    # Avant chaque test, on initialise une variable locale 'p' à 0, qui sera
                    # écrasée dynamiquement par la valeur du calcul.
                    p = 0
                    
                    # Pour chaque structure parenthésée d'expression, on utilise exec pour
                    # assigner à 'p' la valeur de l'expression composée des variables a,b,c,d
                    # et des opérateurs i,j,k, selon la disposition des parenthèses.
                    # exec() exécute une string comme code Python.
                    #
                    # Le test 'exec(...) is None' est toujours True car exec ne retourne rien,
                    # ce qui autorise à enchainer avec la condition 'and p == 10' 
                    # pour vérifier si le résultat du calcul vaut 10.
                    #
                    # Si le résultat est bien 10, on affiche la formule correspondante, avec
                    # les parenthèses correctes pour refléter la priorité d'évaluation.
                    # On utilise la méthode string.format() avec indices positionnels
                    # pour insérer les valeurs et opérateurs dans la chaîne correctement.
                    #
                    # Ensuite, on met 'cont = 0' pour stopper toutes les boucles car on a trouvé
                    # une solution valide.

                    if exec("p = (a{}b){}c{}d".format(i,j,k)) is None and p == 10:
                        print("({0}{4}{1}){5}{2}{6}{3}".format(a,b,c,d,i,j,k))
                        cont = 0
                    elif exec("p = (a{}b{}c){}d".format(i,j,k)) is None and p == 10:
                        print("({0}{4}{1}{5}{2}){6}{3}".format(a,b,c,d,i,j,k))
                        cont = 0
                    elif exec("p = a{}(b{}c){}d".format(i,j,k)) is None and p == 10:
                        print("{0}{4}({1}{5}{2}){6}{3}".format(a,b,c,d,i,j,k))
                        cont = 0
                    elif exec("p = a{}(b{}c{}d)".format(i,j,k)) is None and p == 10:
                        print("{0}{4}({1}{5}{2}{6}{3})".format(a,b,c,d,i,j,k))
                        cont = 0
                    elif exec("p = a{}b{}(c{}d)".format(i,j,k)) is None and p == 10:
                        print("{0}{4}{1}{5}({2}{6}{3})".format(a,b,c,d,i,j,k))
                        cont = 0
                    elif exec("p = ((a{}b){}c){}d".format(i,j,k)) is None and p == 10:
                        print("(({0}{4}{1}){5}{2}){6}{3}".format(a,b,c,d,i,j,k))
                        cont = 0
                    elif exec("p = (a{}b){}(c{}d)".format(i,j,k)) is None and p == 10:
                        print("({0}{4}{1}){5}({2}{6}{3})".format(a,b,c,d,i,j,k))
                        cont = 0
                    elif exec("p = a{}((b{}c){}d)".format(i,j,k)) is None and p == 10:
                        print("{0}{4}(({1}{5}{2}){6}{3})".format(a,b,c,d,i,j,k))
                        cont = 0
                    elif exec("p = (a{}(b{}c)){}d".format(i,j,k)) is None and p == 10:
                        print("({0}{4}({1}{5}{2})){6}{3}".format(a,b,c,d,i,j,k))
                        cont = 0
                    elif exec("p = a{}(b{}(c{}d))".format(i,j,k)) is None and p == 10:
                        print("{0}{4}({1}{5}({2}{6}{3}))".format(a,b,c,d,i,j,k))
                        cont = 0
                    elif exec("p = a{}b{}c{}d".format(i,j,k)) is None and p == 10:
                        print("{0}{4}{1}{5}{2}{6}{3}".format(a,b,c,d,i,j,k))
                        cont = 0

    # Si aucune des combinaisons n'a permis d'obtenir le résultat 10,
    # la variable cont sera restée égale à 1.
    # Dans ce cas, on imprime "0" pour indiquer l'absence de solution.
    if cont == 1:
        print("0")