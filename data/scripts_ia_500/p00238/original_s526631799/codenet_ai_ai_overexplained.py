import sys  # Importe le module sys, qui permet d'interagir avec l'interpréteur Python, notamment pour quitter le programme.
while True:  # Boucle infinie, elle tourne sans fin jusqu'à ce qu'on rencontre une instruction pour sortir (break ou sys.exit).
    t = input()  # Lit une ligne depuis l'entrée standard et l'interprète comme une expression Python (par exemple un entier).
    if t == 0:  # Si la valeur lue est égale à 0 (ce qui sert de condition d'arrêt)... 
        sys.exit(0)  # ... on quitte immédiatement le programme avec un code de sortie 0 (indiquant une sortie sans erreur).
    # La ligne suivante va modifier t en soustrayant la somme d'écarts calculés à partir d'entrées suivantes.
    # On va détailler chaque partie:
    #    input() dans xrange(input()): lit le nombre de lignes suivantes à traiter.
    #    [map(int, raw_input().split()) for i in xrange(input())]: crée une liste où chaque élément est un itérable de deux entiers.
    #    lambda x: x[1] - x[0]: fonction qui calcule la différence entre le deuxième et le premier élément d'un couple.
    #    map(...): applique cette fonction à tous les couples extraits, produisant une séquence de différences.
    #    sum(...): somme toutes ces différences.
    t -= sum(map(lambda x: x[1] - x[0], [map(int, raw_input().split()) for i in xrange(input())]))
    # Après la soustraction, on vérifie la nouvelle valeur de t pour décider de l'affichage.
    if t <= 0:  # Si le résultat est inférieur ou égal à zéro...
        print "OK"  # ... cela signifie que la "tolérance" est atteinte ou dépassée: on imprime OK.
    else:  # Sinon (la valeur est strictement positive)...
        print t  # ... on affiche simplement la valeur restante de t (ce qu'il reste "d'acceptable").