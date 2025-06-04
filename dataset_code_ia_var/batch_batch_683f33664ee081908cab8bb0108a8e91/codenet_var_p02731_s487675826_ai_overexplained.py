import math  # Importe le module math qui fournit des fonctions mathématiques, bien que non utilisé ici

# Demande à l'utilisateur de saisir une valeur, qui sera interprétée comme une chaîne de caractères (str)
# input() affiche une invite à l'utilisateur et attend qu'il saisisse quelque chose au clavier puis appuie sur 'Entrée'
# float() convertit cette chaîne de caractères en un nombre à virgule flottante (nombre décimal)
L = float(input())

# Calcule le cube de la valeur L, c'est-à-dire L multiplié par L puis multiplié encore par L (L * L * L)
# Utilise l'opérateur d'exponentiation ** pour élever L à la puissance 3
# Divise le résultat par 27.0, qui est un nombre flottant représentant 27 comme décimal (plutôt que 27 entier)
resultat = L ** 3 / 27.0  # Le calcul est effectué ici et stocké dans la variable 'resultat'

# Affiche le résultat précédemment calculé à l'écran
# print() affiche une valeur à la console
# '{:.10f}'.format(resultat) formate le nombre pour l'afficher avec exactement 10 chiffres après la virgule
# {:.10f} est un format de chaîne où {:} indique une valeur à formater, .10f signifie "dix chiffres après la virgule"
print('{:.10f}'.format(resultat))
# La sortie sera donc un nombre à virgule flottante affiché précisément à 10 décimales