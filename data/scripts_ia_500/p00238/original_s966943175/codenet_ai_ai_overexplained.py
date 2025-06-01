# Démarrage d'une boucle infinie, ce qui signifie que le bloc de code à l'intérieur sera répété indéfiniment 
# jusqu'à ce que nous rencontrions une instruction "break" qui interrompt cette boucle explicitement.
while 1:
    # Lecture d'une entrée utilisateur au format chaîne de caractères via la fonction input()
    # Conversion immédiate de cette chaîne en un entier à l'aide de la fonction int()
    # Attribution de cet entier à la variable 'a'
    a = int(input())
    
    # Condition qui vérifie si la valeur de 'a' est égale à 0
    # Le double signe égal (==) sert à comparer l'égalité entre deux valeurs
    if a == 0:
        # Si 'a' est égal à 0, on sort de la boucle infinie avec l'instruction 'break'
        # Cela arrête définitivement l'exécution de la boucle while
        break
    
    # Lecture d'une nouvelle entrée utilisateur convertie en entier, puis assignée à la variable 'b'
    b = int(input())
    
    # Début d'une boucle for s'exécutant 'b' fois
    # L'underscore '_' est une variable temporaire souvent utilisée lorsque le compteur n'a pas besoin d'être utilisé
    for _ in range(b):
        # Lecture d'une entrée utilisateur contenant plusieurs nombres séparés par des espaces
        # La méthode split() divise la chaîne à chaque espace et retourne une liste de sous-chaînes
        # map(int, ...) applique la fonction int() sur chaque élément de cette liste pour les convertir en entiers
        # list(...) convertit le résultat de map en une liste concrète d'entiers
        # Cette liste est assignée à la variable 'c'
        c = list(map(int, input().split()))
        
        # Modification de la variable 'a' en soustrayant la différence entre le deuxième élément et le premier élément de 'c'
        # Indices débutent à 0, donc c[1] est le deuxième élément, c[0] le premier
        # La différence correspond à c[1] - c[0]
        a -= c[1] - c[0]
    
    # Après avoir effectué 'b' itérations et modifié 'a' à chaque fois,
    # on affiche le résultat selon deux cas avec une expression conditionnelle ternaire:
    # Si 'a' est strictement supérieur à 0, affiche la valeur de 'a'
    # Sinon, affiche la chaîne de caractères 'OK'
    print(a if a > 0 else 'OK')