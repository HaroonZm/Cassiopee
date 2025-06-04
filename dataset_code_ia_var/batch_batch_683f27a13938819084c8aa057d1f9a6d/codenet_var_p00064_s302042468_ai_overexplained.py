import re  # On importe le module 're' qui permet de manipuler des expressions régulières en Python.

S = 0  # On initialise une variable entière 'S' à 0. Elle servira à accumuler la somme de tous les nombres trouvés.

while True:  # On crée une boucle infinie qui sera interrompue manuellement.
    try:  # On utilise un bloc try-except pour gérer une éventuelle fin d'entrée (EOFError).
        x = input()  # On lit une ligne de texte depuis l'entrée standard. C'est une chaîne de caractères.
        R = re.compile("\d+")  # On compile une expression régulière qui recherche une ou plusieurs chiffres consécutifs.
        # Cette expression signifie :
        # \d : un chiffre (de 0 à 9)
        # +  : une ou plusieurs fois
        m = R.findall(x)  # On utilise la méthode 'findall' pour trouver toutes les sous-chaînes correspondant à l'expression régulière dans 'x'.
        # Cela retourne une liste de chaînes de caractères, chacune représentant un nombre entier trouvé dans la ligne.
        M = [int(s) for s in m]  # On utilise une compréhension de liste :
        # Pour chaque chaîne 's' dans la liste 'm', on convertit 's' en entier avec int(s),
        # et on construit une nouvelle liste 'M' contenant tous ces entiers.
        S += sum(M)  # On utilise la fonction 'sum' pour additionner tous les éléments de la liste 'M',
        # puis on ajoute cette somme à la variable 'S'.
    except EOFError:  # Si jamais la lecture avec input() déclenche une exception EOFError,
        break  # On quitte la boucle infinie avec l'instruction 'break'.
# À ce stade, après la boucle, toutes les lignes ont été lues et tous les nombres additionnés dans 'S'.
print(S)  # On affiche sur la sortie standard la somme totale déréférencée par la variable 'S'.