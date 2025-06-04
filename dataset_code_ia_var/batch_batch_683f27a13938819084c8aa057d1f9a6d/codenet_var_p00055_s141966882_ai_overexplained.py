# Démarre une boucle infinie qui se poursuivra jusqu'à ce qu'une instruction break soit exécutée.
while True:
    try:
        # Demande à l'utilisateur de saisir une valeur via la console. La fonction input() attend une entrée clavier.
        # La chaîne saisie est convertie en nombre à virgule flotante grâce à float().
        # Si la saisie n'est pas convertible en float(), par exemple si l'utilisateur entre une chaîne non-numérique,
        # une exception sera levée.
        a = float(input())
    except:
        # Si une exception survient (par exemple ValueError ou EOFError),
        # on sort de la boucle infinie grâce à l'instruction break.
        break

    # On crée une variable 'total' pour stocker la somme cumulée.
    # On l'initialise avec la valeur saisie par l'utilisateur, qui est 'a'.
    total = a

    # On utilise une boucle for pour répéter un bloc d'instructions.
    # La fonction range(2, 11) renvoie une séquence d'entiers allant de 2 (inclus) à 11 (exclu), donc de 2 à 10.
    # 'i' prendra successivement les valeurs 2, 3, 4, 5, 6, 7, 8, 9, 10.
    for i in range(2, 11):

        # On calcule une variable temporaire 'tmp' à chaque itération.
        # 'a / 3' divise la valeur courante de 'a' par 3.
        # 'i % 2' effectue le modulo 2 sur la valeur 'i', c'est-à-dire le reste de la division de 'i' par 2.
        # Cela retourne 0 si 'i' est pair, 1 si 'i' est impair.
        # '(i % 2)' est donc égal à 1 si 'i' est impair, 0 sinon.
        # 'a * 2' multiplie la valeur de 'a' par 2.
        # '(i % 2 == 0)' est une expression logique évaluée à True si 'i' est pair, False sinon.
        # En Python, True équivaut à 1 et False à 0 dans un contexte arithmétique.
        # Donc '(a * 2) * (i % 2 == 0)' aura la valeur 'a * 2' seulement si 'i' est pair, 0 sinon.
        # Finalement, 'tmp' prend la somme de deux termes :
        # 1. (a / 3), uniquement si 'i' est impair.
        # 2. (a * 2), uniquement si 'i' est pair.
        tmp = (a / 3) * (i % 2) + (a * 2) * (i % 2 == 0)

        # On ajoute la valeur de 'tmp' à la variable 'total' pour accumuler le résultat au fil des itérations.
        total += tmp

        # On assigne à 'a' la valeur nouvellement calculée 'tmp', afin de faire évoluer 'a'
        # à chaque itération suivant une relation de récurrence.
        a = tmp

    # Après la fin de la boucle for, donc après avoir exécuté le bloc pour tous les 'i' de 2 à 10,
    # on affiche la valeur finale de 'total' à l'aide de la fonction print(),
    # ceci écrit la sortie dans la console, suivi d'un retour à la ligne.
    print(total)