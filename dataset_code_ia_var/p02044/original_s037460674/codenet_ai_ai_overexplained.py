# Démarre une boucle infinie; cela permet d'exécuter indéfiniment le bloc tant que la boucle n'est pas rompue explicitement
while True:
    # Attend une saisie utilisateur sous forme de chaîne, la découpe en morceaux à chaque espace,
    # puis convertit chaque morceau en un entier avec map(int, ...), 
    # enfin affecte ces deux entiers aux variables n et m respectivement.
    n, m = map(int, input().split())
    
    # Condition pour sortir de la boucle : si n et m valent tous deux zéro
    if (n, m) == (0, 0):
        # 'break' interrompt la boucle en cours et continue avec le reste du code après la boucle
        break
    
    # Calcule combien de fois 'n' tient dans 'm' sans reste, c'est-à-dire la division entière (//)
    t = m // n
    
    # Demande à l'utilisateur une nouvelle ligne d'entrée, la découpe en morceaux à chaque espace,
    # convertit chaque morceau en entier et crée une liste avec ces entiers. 
    # Ceci peut être vu comme la conversion d'une ligne de nombres séparés par des espaces en une liste d'entiers.
    a = list(map(int, input().split()))
    
    # Initialise une variable appelée 'cnt' pour compter la somme totale requise, partant de zéro
    cnt = 0
    
    # Commence une itération sur chaque élément 'i' de la liste 'a'. Chaque 'i' représente un entier de la liste.
    for i in a:
        # Si t est inférieur ou égal à i, cela signifie qu'on ne peut pas prendre plus que 't'.
        if t <= i:
            # Ajoute 't' à 'cnt' car cela représente la quantité maximale autorisée à ajouter.
            cnt += t
        else:
            # Dans le cas contraire (si i < t), on ajoute 'i' à 'cnt', c'est-à-dire la totalité de ce qui est disponible.
            cnt += i
    
    # Affiche la valeur finale de 'cnt' à l'écran, pour l'utilisateur.
    print(cnt)