# Commencer une boucle infinie. Cela garantit que le bloc de code à l'intérieur continue à s'exécuter sans fin,
# jusqu'à ce qu'une instruction de sortie explicite (comme break) soit rencontrée.
while True:
    # Lire une ligne de texte de l'utilisateur via la console avec la fonction input().
    # Cette fonction lit l'entrée utilisateur sous forme de chaîne de caractères (string).
    # La méthode split() découpe cette chaîne en une liste de sous-chaînes, séparées par des espaces.
    # Ici, on suppose que l'utilisateur saisit une expression de la forme "a op b" (ex : "4 + 2").
    # On affecte respectivement le premier élément à 'a', le deuxième à 'op' (l'opérateur), et le troisième à 'b'.
    a, op, b = input().split()

    # Convertir 'a' (qui est actuellement de type string) en entier (int),
    # afin de pouvoir effectuer des opérations arithmétiques.
    a = int(a)

    # Convertir 'b' en entier pour la même raison.
    b = int(b)

    # Vérifier si l'opérateur (op) saisi par l'utilisateur est un point d'interrogation '?'
    # Ceci agit comme une condition d'arrêt pour quitter la boucle infinie.
    if op == '?':
        # Si c'est le cas, on utilise 'break' pour sortir de la boucle while.
        break

    # Vérifier si l'opérateur est le symbole '+' (addition).
    elif op == '+':
        # Si c'est le cas, effectuer l'addition de 'a' et 'b', puis afficher le résultat à l'écran avec print().
        print(a + b)

    # Vérifier si l'opérateur est '-' (soustraction).
    elif op == '-':
        # Effectuer la soustraction : 'a' moins 'b', afficher le résultat.
        print(a - b)

    # Vérifier si l'opérateur est '*' (multiplication).
    elif op == '*':
        # Effectuer la multiplication : 'a' fois 'b', afficher le résultat.
        print(a * b)

    # Vérifier si l'opérateur est '/' (division entière).
    elif op == '/':
        # Effectuer la division entière de 'a' par 'b' (l'opérateur / réalise la division flottante,
        # int() convertit le résultat en valeur entière, supprimant la partie décimale).
        print(int(a / b))

    # Aucun autre opérateur n'est prévu,
    # donc si un opérateur inattendu est entré, rien ne se passe et la boucle recommence.