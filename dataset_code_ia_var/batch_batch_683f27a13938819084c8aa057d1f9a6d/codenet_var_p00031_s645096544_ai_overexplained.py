# Commence une boucle infinie, ce qui veut dire que ce bloc de code va être répété indéfiniment jusqu'à ce qu'une interruption (break) se produise.
while 1:
    try:
        # Tente d'obtenir une entrée de l'utilisateur (au clavier) via la fonction input().
        # Cette entrée est lue comme une chaîne de caractères.
        # int() convertit cette chaîne de caractères en nombre entier.
        n = int(input())
        
        # Initialise une liste vide nommée 'ans'.
        # Cette liste va servir à stocker certains nombres que l'on va calculer dans la suite du programme.
        ans = []
        
        # for i in range(10) lance une boucle qui fait varier la variable i de 0 à 9 (inclus).
        # Cela signifie que ce bloc sera exécuté dix fois pour i = 0, 1, 2, ..., 9.
        for i in range(10):
            
            # 2**(9-i) calcule la puissance de 2 correspondant à l'(9-i)-ème bit de poids fort dans un nombre binaire sur 10 bits.
            # Par exemple, si i = 0, alors 2**(9-0) = 2**9 = 512.
            # Si n (notre nombre courant) est supérieur ou égal à cette puissance de 2,
            # alors nous allons effectuer les instructions du bloc if.
            if n >= 2**(9 - i):
                
                # Si la condition est vraie, on ajoute (append) la puissance de 2 calculée à la liste 'ans'.
                ans.append(2**(9 - i))
                
                # On soustrait (décrémente) le même montant à n afin de traiter le reste du nombre.
                n -= 2**(9 - i)
        
        # La fonction map applique la fonction str (conversion en chaîne de caractères) à chaque élément de la liste ans[::-1].
        # ans[::-1] crée une nouvelle liste qui est une version inversée de ans, c'est-à-dire que le premier élément devient le dernier, et ainsi de suite.
        # ' '.join(..) prend chaque élément (qui est maintenant une chaîne) et les rassemble en une seule grande chaîne,
        # séparant chaque élément par un espace.
        # Enfin, print affiche la chaîne résultante à l'écran.
        print(' '.join(map(str, ans[::-1])))
    
    # except est utilisé pour attraper et traiter les erreurs potentielles qui pourraient survenir dans le bloc try précédent.
    # Ici, aucune exception spécifique n'est mentionnée : toutes les erreurs possibles amènent à exécuter le bloc except.
    # break interrompt la boucle infinie while et sort du programme (ou de la boucle).
    except:
        break