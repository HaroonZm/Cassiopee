# Début d'une boucle infinie, ce qui signifie qu'elle continuera à s'exécuter sans arrêt
# jusqu'à ce qu'une condition de sortie explicite soit rencontrée (par exemple, un break)
while True:
    # Initialisation des variables a et b à zéro au début de chaque itération de la boucle
    # Ces variables vont stocker des sommes cumulées qui seront calculées plus tard
    a = b = 0
    
    # Lecture d'une entrée utilisateur via la fonction input()
    # L'entrée est supposée être une chaîne de caractères représentant un nombre entier
    # La fonction int() convertit cette chaîne en un nombre entier pour traitement numérique
    n = int(input())
    
    # Vérification si la valeur entière saisie est égale à zéro
    # Si c'est le cas, cela signifie qu'on souhaite sortir de la boucle infinie (fin du programme)
    if n == 0:
        # Instruction break qui permet de sortir immédiatement de la boucle while
        break
    
    # Démarrage d'une boucle for qui va s'exécuter n fois,
    # c'est-à-dire n itérations correspondant au nombre saisi précédemment
    # La variable i prend successivement les valeurs de 0 à n-1 (non utilisée ici dans le corps)
    for i in range(n):
        # Lecture d'une nouvelle ligne d'entrée utilisateur contenant deux entiers séparés par un espace
        # La méthode split() divise cette chaîne en morceaux, ici deux, sur le caractère espace
        # La fonction map(int, ...) applique int() à chacun des morceaux pour les convertir en entiers
        # On affecte ces deux entiers convertis aux variables c et d via unpacking
        c, d = map(int, input().split())
        
        # Comparaison de la variable c avec la variable d
        if c > d:
            # Si c est strictement supérieur à d, on ajoute à a la somme de c et d
            a += c + d
        elif c < d:
            # Sinon, si c est strictement inférieur à d, on ajoute à b la somme de c et d
            b += c + d
        else:
            # Sinon cela signifie que c est égal à d
            # Dans ce cas, on ajoute c à a
            a += c
            # Et on ajoute d à b ; puisque c=d, la contribution est divisée équitablement
            b += d
    
    # Une fois la boucle for terminée, on affiche les valeurs finales de a et b séparées par un espace
    # La fonction print() envoie la sortie à la console sous forme lisible pour l'utilisateur
    print(a, b)