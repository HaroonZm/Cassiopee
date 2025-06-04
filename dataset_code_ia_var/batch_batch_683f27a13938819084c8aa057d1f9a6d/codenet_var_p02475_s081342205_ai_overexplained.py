# Demande à l'utilisateur de saisir deux entiers séparés par un espace
# La fonction input() lit la ligne saisie par l'utilisateur au clavier (par défaut en texte [str])
# La méthode split() découpe la chaîne de caractères en une liste de sous-chaînes sur les espaces par défaut
# La fonction map() applique la fonction int() à chaque élément de cette liste pour les convertir en entiers
# L'affectation multiple a, b = ... attribue respectivement le premier et second entier aux variables a et b
a, b = map(int, input().split())

# Vérifie si les deux nombres (a et b) ont le même signe (tous les deux négatifs ou tous les deux positifs)
# (a < 0) est True si a est négatif, False sinon, idem pour (b < 0)
# L'opérateur == renvoie True si les deux sont identiques (donc même signe) et False sinon
# L'opérateur conditionnel (ternaire) "1 if ... else -1" donne 1 si même signe, sinon -1
# Ce résultat est stocké dans la variable sign : il sert à ajuster le signe du résultat final
sign = 1 if (a < 0) == (b < 0) else -1

# Remplace la valeur de a par sa valeur absolue (sans le signe), donc a devient positif
a = abs(a)
# Remplace la valeur de b par sa valeur absolue (sans le signe), donc b devient positif
b = abs(b)

# Effectue la division entière de a par b grâce à l'opérateur //
# Cela renvoie le quotient de la division sans le reste, c'est-à-dire la partie entière
# Multiplie le résultat par sign pour appliquer le bon signe final
# La fonction print() affiche le résultat à l'utilisateur à l'écran
print((a // b) * sign)