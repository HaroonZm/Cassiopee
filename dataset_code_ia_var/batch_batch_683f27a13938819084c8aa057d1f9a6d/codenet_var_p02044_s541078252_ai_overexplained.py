# On utilise une boucle while qui s'exécutera indéfiniment jusqu'à ce que l'on utilise une instruction break pour quitter la boucle
while True:
    # Lecture d'une ligne de l'entrée standard avec la fonction input()
    # La méthode split() découpe la chaîne d'entrée en utilisant l'espace comme séparateur, produisant une liste de chaînes
    # La fonction map(int, ...) transforme chaque élément de la liste découpée en un entier
    # Les deux premiers entiers sont affectés respectivement aux variables n et m
    n, m = map(int, input().split())
    # On vérifie si à la fois n et m valent 0 (ce qui sert de condition d'arrêt pour arrêter le traitement)
    if n == 0 and m == 0:
        # L'instruction break permet de sortir immédiatement de la boucle while (c'est-à-dire d'arrêter le programme)
        break
    # Lecture d'une nouvelle ligne de l'entrée standard servant à obtenir la liste des entiers
    # input() lit la ligne
    # split() sépare cette ligne en morceaux sur chaque espace
    # La compréhension de liste [int(x) for x in ...] parcourt chaque fragment et le convertit en int pour former une nouvelle liste d'entiers
    a = [int(x) for x in input().split()]
    # On initialise une variable ans à zéro, pour accumuler la somme finale selon les règles du problème
    ans = 0
    # On commence une boucle for pour parcourir tous les éléments de la liste a
    for i in a:
        # On vérifie si la valeur courante i est strictement inférieure à la division entière de m par n
        # La division entière m//n donne le résultat de m divisé par n sans reste, c'est-à-dire un quotient entier arrondi vers le bas
        if i < m // n:
            # Si la condition est vraie, alors on ajoute simplement la valeur i courante à la variable ans
            ans += i
        else:
            # Sinon, si i est supérieur ou égal à m//n, on ajoute seulement m//n à ans (c'est-à-dire on limite la valeur maximale ajoutée)
            ans += m // n
    # On affiche la valeur finale accumulée dans ans pour ce cas de test particulier à l'aide de la fonction print
    print(ans)