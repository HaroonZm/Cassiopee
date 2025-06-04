# Demande à l'utilisateur de saisir une chaîne de caractères.
# La fonction raw_input() lit l'entrée en tant que chaîne de caractères (cela fonctionne pour Python 2.x).
# L'appel à .strip() supprime les espaces ou caractères de nouvelle ligne du début et de la fin de la chaîne.
line = raw_input().strip()

# La fonction reversed() prend un objet itérable (comme une chaîne) et renvoie un nouvel itérateur qui traverse les éléments dans l'ordre inverse.
# La fonction reduce() applique successivement une fonction binaire (ici une fonction lambda qui concatène deux caractères) aux éléments de l'itérable,
# de gauche à droite, pour réduire l'itérable à une seule valeur (ici, une chaîne inversée).
# La lambda prend deux arguments 'a' et 'b' et renvoie leur addition : a + b, ce qui correspond à la concaténation de chaînes.
# La fonction print affiche le résultat de cette réduction à l'écran.
print reduce(
    # La fonction lambda indique comment réduire deux éléments : les joindre ('a' + 'b').
    lambda a, b: a + b, 
    # On passe à reduce l'itérateur inversé de la ligne d'entrée, ce qui retournera la chaîne inversée.
    reversed(line)
)