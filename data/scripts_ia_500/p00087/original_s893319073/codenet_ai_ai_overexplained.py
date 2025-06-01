def solve(st):
    # La fonction 'solve' prend en entrée une chaîne de caractères 'st'
    # qui représente une expression en notation polonaise inversée (postfixe).
    # L'objectif est de calculer la valeur numérique de cette expression.
    
    d = st.split()
    # On utilise la méthode 'split()' sur la chaîne 'st' pour obtenir une liste de sous-chaînes.
    # Chaque élément de cette liste est un opérande ou un opérateur.
    # 'split()' sans argument sépare la chaîne selon les espaces.
    # Exemple : "3 4 +" devient ["3", "4", "+"]
    
    l = []
    # On initialise une liste vide 'l' qui servira de pile pour le calcul.
    # La pile est une structure de données qui suit le principe LIFO (Last In, First Out).
    # On y stocke temporairement les nombres calculés ou extraits.
    
    for i in xrange(len(d)):
        # 'xrange(len(d))' crée un itérateur allant de 0 à la longueur de la liste 'd' - 1.
        # On itère donc sur chaque index 'i' correspondant à chaque élément de 'd'.
        
        if d[i] == "+":
            # Si l'élément courant est le caractère '+' (opérateur addition)
            # On doit appliquer l'addition en dépilant les deux derniers nombres de la pile.
            
            l.append(l.pop() + l.pop())
            # 'l.pop()' enlève et retourne le dernier élément de la liste 'l'.
            # Ici, on dépile deux éléments : le dernier et l'avant-dernier.
            # Ensuite, on les additionne, et on empile (append) le résultat.
            # Attention : l'ordre d'opération est important en arithmétique.
            # Comme l'opération est commutative pour '+', ici l'ordre ne change pas le résultat.
        
        elif d[i] == "-":
            # Si l'élément est le caractère '-' (opérateur soustraction)
            
            l.append(-l.pop() + l.pop())
            # On dépile le premier nombre (disons 'a') avec l.pop(), puis on le multiplie par -1 => (-a)
            # Ensuite on dépile le second nombre (disons 'b') avec l.pop()
            # Enfin on effectue 'b + (-a)' ce qui équivaut à 'b - a'
            # Cela respecte le bon ordre des opérandes pour la soustraction.
        
        elif d[i] == "*":
            # Si l'élément est '*', opérateur multiplication
            
            l.append(l.pop() * l.pop())
            # On dépile deux nombres et on les multiplie.
            # La multiplication est commutative, donc l'ordre des dépilages n'affecte pas le résultat.
        
        elif d[i] == "/":
            # Si l'élément est '/', opérateur division
            
            l.append(1 / l.pop() * l.pop())
            # Ici, on dépile le diviseur en dernier (appelons-le 'a'), avec l.pop()
            # On calcule son inverse 1/a
            # Puis on dépile le dividende en avant-dernier (appelons-le 'b')
            # Enfin on multiplie 'b * (1/a)', ce qui vaut 'b / a'
            # Cette façon de faire garantit le bon ordre dans la division.
        
        else:
            # Si l'élément n'est pas un opérateur reconnu, on considère que c'est un nombre.
            
            l.append(float(d[i]))
            # On convertit la chaîne en nombre flottant avec float().
            # Puis on empile ce nombre sur la pile 'l'.
    
    return l[0]
    # Après avoir traité tous les éléments, il ne reste qu'un seul élément dans la pile,
    # qui est le résultat final de l'expression.
    # On le retourne.


while True:
    # Une boucle infinie 'while True' sert à lire des entrées en continu.
    
    try:
        s = raw_input()
        # On essaie de récupérer une ligne de texte depuis l'entrée standard.
        # 'raw_input()' lit une ligne entière jusqu'au retour à la ligne.
        # Si l'utilisateur entre EOF (fin de fichier), une exception sera levée.

        print solve(s)
        # On appelle la fonction 'solve' en lui passant cette ligne,
        # et on affiche le résultat au format texte avec 'print'.
    
    except:
        # En cas d'exception (notamment d'EOF lorsque l'utilisateur arrête la saisie)
        break
        # On sort de la boucle infinie, et donc le programme se termine.