# Commencer une boucle infinie qui répétera son contenu sans fin à moins d'une interruption explicite avec une instruction 'break'
while True:
    # Demander à l'utilisateur d'entrer une ligne de texte via la fonction input().
    # Cette ligne devrait contenir trois éléments séparés par des espaces : un nombre, un opérateur (+, -, *, / ou ?) et un autre nombre.
    # La méthode split() divise la ligne d'entrée en une liste de sous-chaînes en coupant sur les espaces.
    # La fonction map(str, ...) applique la fonction str à chaque élément, mais l'entrée est déjà une chaîne, donc cela est en fait superflu.
    # L'opérateur de décompactage (a, op, b =) permet d'assigner respectivement les trois éléments reçus à trois variables distinctes : 'a', 'op' et 'b'.
    a, op, b = map(str, input().split())
    
    # Vérifier si la variable 'op' contient le caractère '?'
    # Si c'est le cas, cela indique à notre programme de s'arrêter.
    if(op == '?'):
        # L'instruction break force la sortie immédiate de la boucle la plus proche, ici, notre boucle while True.
        break

    # Début d'une chaîne de conditions pour vérifier quel opérateur l'utilisateur a entré
    # Si l'opérateur saisi est le symbole '+', on effectue une addition
    if(op == "+"):
        # Conversion de 'a' et 'b', qui sont des chaînes de caractères représentant des nombres, en entiers via la fonction int()
        # On additionne ensuite ces deux entiers
        # La fonction print() affiche le résultat (la somme) à l'écran
        print(int(a) + int(b))
    # Si l'opérateur est le symbole '-', effectuer une soustraction
    elif(op == "-"):
        # Même conversion explicite des opérandes de la chaîne vers le type entier
        # Calcul de la différence, puis impression du résultat
        print(int(a) - int(b))
    # Si l'opérateur est le symbole '*', effectuer une multiplication
    elif(op == "*"):
        # Conversion des opérandes en entiers, multiplication, puis affichage du produit
        print(int(a) * int(b))
    # Si l'opérateur est le symbole '/', effectuer une division entière
    elif(op == "/"):
        # Convertit les deux opérandes en entiers, puis exécute une division entière (quotient sans le reste)
        # L'opérateur // signifie division entière, ce qui donne le résultat arrondi vers le bas à l'entier le plus proche
        print(int(a) // int(b))
    # (Il n'y a pas de clause else finale : si un opérateur inconnu est entré, rien ne se passe)