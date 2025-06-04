# Demande à l'utilisateur de saisir une valeur entière
# La fonction input() affiche une invite à l'utilisateur et retourne la saisie sous forme de chaîne de caractères
# int() convertit cette chaîne de caractères en un entier (nombre entier)
L = int(input())

# Calcule le cube de L, c'est-à-dire L * L * L (ce qui revient à élever L à la puissance 3)
# Puis divise ce résultat par 27
# L'opérateur * est utilisé pour la multiplication
# L'opérateur / est utilisé pour la division et donne un résultat à virgule flottante
# print() affiche le résultat final à l'écran
print(L * L * L / 27)