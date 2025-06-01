def calculer_cout_minimal():
    """
    Lit un nombre entier n représentant le nombre de cas de test.
    Pour chaque cas, lit les entiers x, y, b, p, calcule et affiche un coût minimal en fonction de certaines conditions tarifaires.

    Entrées attendues :
        - n : int, nombre de cas de test
        - Pour chaque cas, une ligne contenant quatre entiers séparés par des espaces : x, y, b, p

    Sortie :
        - Pour chaque cas, affiche un entier représentant le coût minimal calculé.
    """
    n = int(input())
    for i in range(n):
        # Lire les valeurs x, y, b, p depuis l'entrée standard
        x, y, b, p = map(int, input().split())
        
        # Calcul du coût initial 's' sans réduction
        # s = x multiplié par b + y multiplié par p
        s = x * b + y * p
        
        # Calcul d'une estimation 't' d'un coût avec une réduction fixe à 80%
        # t est égal à 80% de (5 fois x + 2 fois y)
        t = int((x * 5 + y * 2) * 0.8)
        
        # Initialisation de la variable 'u' qui représente un coût ajusté
        u = s
        
        # Si le coût initial 's' est inférieur ou égal à l'estimation 't'
        if s <= t:
            # Afficher directement le coût initial 's'
            print(s)
        else:
            # Sinon, appliquer certains ajustements sur le coût 'u' en fonction des écarts de tarifs
            # Si b est inférieur à 5, ajouter le coût supplémentaire pour la différence
            if 5 - b > 0:
                u += (5 - b) * x
                
            # Si p est inférieur à 2, ajouter le coût supplémentaire pour la différence
            if 2 - p > 0:
                u += (2 - p) * y
            
            # Afficher le minimum entre le coût initial 's' et 80% du coût ajusté 'u'
            print(min(s, int(u * 0.8)))