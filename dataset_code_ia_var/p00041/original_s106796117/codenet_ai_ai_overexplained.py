from itertools import permutations  # On importe la fonction permutations du module itertools pour générer toutes les permutations d'une liste

while(1):  # Boucle infinie : elle s'arrêtera seulement via un break explicite à l'intérieur
    # On lit une ligne de l'entrée standard (clavier) avec input(),
    # puis on coupe la chaîne obtenue en morceaux selon les espaces avec split()
    # Ensuite, pour chaque morceau obtenu, on le convertit en entier avec int(i)
    # Enfin, on assemble tout ça dans une liste grâce à la compréhension de liste
    a_ = [int(i) for i in input().split()]
    
    # On vérifie si la liste obtenue correspond à quatre zéros [0, 0, 0, 0].
    # Cela signifie qu'on doit arrêter le programme. 
    if a_ == [0,0,0,0]:
        break  # On sort de la boucle et donc le programme s'arrête.
    
    # On génère toutes les permutations possibles des quatre nombres saisis
    # permutations(a_) retourne un itérable de tuples, chacun étant une permutation.
    # Pour chaque tuple, on le transforme en liste pour avoir une uniformité d'accès aux éléments par index ou nom.
    p = list(list(i) for i in permutations(a_))
    
    cont = 1  # Ce flag permet de s'arrêter dès qu'on trouve une solution (évite de trouver plusieurs solutions pour la même entrée)

    # On parcourt la liste complète de permutations
    for a, b, c, d in p:  # À chaque fois, a, b, c, d prennent les valeurs correspondant à une permutation
        
        if cont == 0:
            break  # On sort de cette boucle, car on a déjà trouvé une solution.

        # On essaie toutes les combinaisons possibles de trois opérateurs, i, j, k.
        # Ils prennent chacun tour à tour la valeur "+", "-", ou "*"
        for i in ("+","-","*"):
            if cont == 0:
                break  # On regarde toujours si un résultat a déjà été trouvé, pour arrêter.
            for j in ("+","-","*"):
                if cont == 0:
                    break
                for k in ("+","-","*"):
                    if cont == 0:
                        break
                    
                    # On initialise une variable p à 0 (elle récupérera le résultat du calcul)
                    p = 0
                    
                    # On va essayer 11 parenthésages/arbre de calcul différents possibles pour 4 nombres et 3 opérateurs
                    # À chaque fois, on évalue dynamiquement une expression arithmétique
                    # exec exécute dynamiquement du code Python sous forme de chaîne de caractères.
                    # On utilise .format(...) pour insérer les valeurs et opérateurs à leur place correcte.

                    # Les tests "is None" servent à s'assurer qu'exec ne retourne pas d'erreur (car exec retourne toujours None sauf exception)
                    # Après exec, p est modifié (car exec agit sur la variable p définie juste avant)
                    # On vérifie que le résultat vaut 10, alors on affiche l'expression correspondante, sinon on continue

                    # Cas 1 : (a op1 b) op2 c op3 d
                    if exec("p = (a{}b){}c{}d".format(i,j,k)) is None and p == 10:
                        print("({0}{4}{1}){5}{2}{6}{3}".format(a,b,c,d,i,j,k))
                        cont = 0  # On indique qu'on a trouvé une solution, donc on arrête.
                    # Cas 2 : (a op1 b op2 c) op3 d
                    elif exec("p = (a{}b{}c){}d".format(i,j,k)) is None and p == 10:
                        print("({0}{4}{1}{5}{2}){6}{3}".format(a,b,c,d,i,j,k))
                        cont = 0
                    # Cas 3 : a op1 (b op2 c) op3 d
                    elif exec("p = a{}(b{}c){}d".format(i,j,k)) is None and p == 10:
                        print("{0}{4}({1}{5}{2}){6}{3}".format(a,b,c,d,i,j,k))
                        cont = 0
                    # Cas 4 : a op1 (b op2 c op3 d)
                    elif exec("p = a{}(b{}c{}d)".format(i,j,k)) is None and p == 10:
                        print("{0}{4}({1}{5}{2}{6}{3})".format(a,b,c,d,i,j,k))
                        cont = 0
                    # Cas 5 : a op1 b op2 (c op3 d)
                    elif exec("p = a{}b{}(c{}d)".format(i,j,k)) is None and p == 10:
                        print("{0}{4}{1}{5}({2}{6}{3})".format(a,b,c,d,i,j,k))
                        cont = 0
                    # Cas 6 : ((a op1 b) op2 c) op3 d
                    elif exec("p = ((a{}b){}c){}d".format(i,j,k)) is None and p == 10:
                        print("(({0}{4}{1}){5}{2}){6}{3}".format(a,b,c,d,i,j,k))
                        cont = 0
                    # Cas 7 : (a op1 b) op2 (c op3 d)
                    elif exec("p = (a{}b){}(c{}d)".format(i,j,k)) is None and p == 10:
                        print("({0}{4}{1}){5}({2}{6}{3})".format(a,b,c,d,i,j,k))
                        cont = 0
                    # Cas 8 : a op1 ((b op2 c) op3 d)
                    elif exec("p = a{}((b{}c){}d)".format(i,j,k)) is None and p == 10:
                        print("{0}{4}(({1}{5}{2}){6}{3})".format(a,b,c,d,i,j,k))
                        cont = 0
                    # Cas 9 : (a op1 (b op2 c)) op3 d
                    elif exec("p = (a{}(b{}c)){}d".format(i,j,k)) is None and p == 10:
                        print("({0}{4}({1}{5}{2})){6}{3}".format(a,b,c,d,i,j,k))
                        cont = 0
                    # Cas 10 : a op1 (b op2 (c op3 d))
                    elif exec("p = a{}(b{}(c{}d))".format(i,j,k)) is None and p == 10:
                        print("{0}{4}({1}{5}({2}{6}{3}))".format(a,b,c,d,i,j,k))
                        cont = 0
                    # Cas 11 : a op1 b op2 c op3 d (aucune parenthèse)
                    elif exec("p = a{}b{}c{}d".format(i,j,k)) is None and p == 10:
                        print("{0}{4}{1}{5}{2}{6}{3}".format(a,b,c,d,i,j,k))
                        cont = 0

    # Après avoir énuméré toutes les combinaisons, si aucune solution n'a été trouvée,
    # cont vaut toujours 1 : on affiche alors "0" pour signaler l'absence de solution.
    if cont == 1:
        print("0")