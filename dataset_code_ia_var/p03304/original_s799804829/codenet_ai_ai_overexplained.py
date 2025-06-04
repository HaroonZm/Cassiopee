# Demander à l'utilisateur de saisir trois entiers séparés par des espaces sur la même ligne.
# Utiliser la fonction input() pour lire cette ligne de texte depuis l'entrée standard (le clavier).
# La méthode split() découpe la chaîne de caractères en une liste de sous-chaînes, en utilisant l'espace comme séparateur par défaut.
# Ensuite, map(int, ...) applique la fonction int() à chaque sous-chaîne pour les convertir en entiers.
# Enfin, on associe ces trois valeurs aux variables n, m et d, respectivement.
n, m, d = map(int, input().split())

# Vérifier si la valeur de d est exactement égale à zéro.
if d == 0:
    # Si c'est le cas, affecter la valeur de n à la variable p.
    # Cela signifie simplement que p et n seront identiques lorsque d vaut 0.
    p = n
else:
    # Dans le cas contraire (c'est-à-dire si d n'est pas égal à 0), calculer p comme suit :
    # Multiplier la valeur de n par 2.
    # Soustraire de ce résultat le double de la valeur de d (c'est-à-dire d multiplié par 2).
    # Attribuer ce résultat à la variable p.
    # Cette opération peut être lue comme : p = (2 * n) - (2 * d)
    p = (n * 2 - d * 2)

# Calculer une valeur r en divisant p par le carré de n (soit n multiplié par lui-même).
# Cette étape utilise l'opérateur de division (/) qui renvoie un nombre à virgule flottante.
r = p / (n * n)

# Calculer une nouvelle valeur a en multipliant r par (m - 1).
# On soustrait 1 à la valeur de m, puis on multiplie le résultat par la variable r.
# Cela permet d'obtenir le résultat final avant l'affichage.
a = r * (m - 1)

# Afficher le résultat de a, arrondi à huit chiffres après la virgule.
# La fonction round() est utilisée pour arrondir a à 8 décimales.
# La fonction print() permet d'afficher ce résultat à l'écran.
print(round(a, 8))