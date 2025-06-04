import sys  # Importe le module sys, qui fournit un accès à certains objets utilisés ou maintenus par l'interpréteur Python

# Boucle sur chaque ligne reçue de l'entrée standard (stdin)
for x in sys.stdin:
    s = 0  # Initialise une variable 's' à 0, elle va servir à accumuler la somme au fil des itérations

    a = float(x)  # Convertit la ligne lue en nombre à virgule flottante (float) et l'assigne à la variable 'a'

    # Boucle qui va répéter ses instructions 10 fois, de i allant de 0 à 9 inclus
    for i in range(10):
        s += a  # Ajoute la valeur courante de 'a' à 's', ce qui met à jour la somme accumulée

        # Vérifie si la variable d'itération 'i' est paire (c'est-à-dire divisible par 2 avec reste 0)
        if i % 2 == 0:
            a *= 2  # Si 'i' est pair, multiplie 'a' par 2 et stocke le résultat toujours dans 'a'
        else:
            a /= 3  # Sinon, si 'i' est impair, divise 'a' par 3 et met à jour la variable 'a' avec ce résultat

    print s  # Affiche la valeur finale de 's' sur la sortie standard, c'est-à-dire l'accumulation selon la logique précédente