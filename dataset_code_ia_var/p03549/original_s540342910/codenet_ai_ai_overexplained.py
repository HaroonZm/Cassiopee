# On commence par demander à l'utilisateur de saisir deux entiers séparés par un espace.
# La fonction input() lit une ligne entrée au clavier sous forme de chaîne de caractères.
# La méthode split() découpe cette chaîne en une liste de sous-chaînes en se basant sur les espaces.
# La fonction map() applique ici la fonction int à chaque sous-chaîne pour les convertir en entiers.
# n et m sont ainsi initialisés par affectation multiple : n reçoit le premier entier, m le second.
n, m = map(int, input().split())

# Calcul du temps pour corriger un lot de 'n' soumissions dont 'm' doivent absolument passer à la fin.
# Pour chaque des 'm' soumissions spéciales, il faut 1900 unités de temps (plus compliqué ou plus long),
# tandis que pour chaque des 'n-m' autres soumissions, il faut seulement 100 unités de temps (plus simple ou plus rapide).
# On multiplie donc m par 1900 pour le temps total de ces soumissions difficiles.
# On multiplie (n-m) par 100 pour le temps total des soumissions plus simples.
# On additionne ces deux quantités pour obtenir le temps total d'une série de soumissions.
x = 1900 * m + 100 * (n - m)  # le temps nécessaire pour traiter une série de soumissions

# Au final, on doit soumettre les réponses jusqu'à réussir toutes les 'm' soumissions exigeantes en dernier.
# Chaque soumission a une chance au plus tôt de réussir du premier coup. Mais à cause des contraintes posées,
# il faut envisager le pire cas où l'on ferait exactement le nombre maximal d'essais possible.
# Ce nombre de tentatives est modélisé par 2 puissance m, car à chaque 'm', la difficulté (ou probabilité d'échec) double.
# On multiplie le temps pour un ensemble de soumissions (x) par 2 puissance m pour obtenir le temps total attendu.
# print() affiche à l'écran ce temps total. L'expression (2**m) calcule 2 à la puissance m.
print(x * (2 ** m))  # affichage du temps total minimum requis pour réussir tous les 'm' cas difficiles à la fin