# Version avec quelques choix de conception non-conventionnels

lambda _: [(__import__('builtins').exec("print('Yes')" if 500*int(__import__('sys').stdin.read().split()[0])>=int(__import__('sys').stdin.read().split()[1]) else "print('No')"))][0](__import__('sys').stdin)

# Notes :
# - Utilisation de __import__('builtins').exec pour contourner l'utilisation directe de exec().
# - Lecture de l'entrée via sys.stdin (deux fois, volontairement non conventionnel !).
# - Tout est en une ligne avec une lambda non utile.
# - Parenthésage "inutile" pour accentuer le style.
# - Utilisation d'un indice sur une liste de taille 1 pour exécuter le code.
# - Pas de variables intermédiaires nommées.