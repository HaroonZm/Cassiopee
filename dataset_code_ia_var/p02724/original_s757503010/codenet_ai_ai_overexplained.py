# On demande à l'utilisateur de saisir une valeur entière via le clavier.
# La fonction input() recueille une chaîne de caractères (string).
# La fonction int() convertit cette chaîne de caractères en un entier (integer).
# Le résultat est stocké dans la variable X.
X = int(input())

# On souhaite déterminer combien de fois 500 peut aller dans X sans dépasser X (division entière).
# L'opérateur // effectue une division entière (le quotient sans la partie décimale).
# Cela donne le nombre de billets de 500.
# On stocke ce résultat dans la variable x.
x = X // 500

# On cherche maintenant le reste de la division de X par 500,
# c'est-à-dire ce qui reste après avoir retiré tout ce qui pouvait être couvert par les billets de 500.
# L'opérateur % retourne le reste.
# Le résultat est stocké dans la variable res.
res = X % 500

# Maintenant, à partir du reste res, on cherche combien de pièces de 5 peuvent y entrer.
# Encore une division entière : res // 5.
# Cela donne le nombre de pièces de 5.
# On stocke ce résultat dans y.
y = res // 5

# On va maintenant calculer le montant total obtenu en additionnant :
# - 1000 fois le nombre de billets de 500 (car chaque billet rapporte 1000 points),
# - 5 fois le nombre de pièces de 5 (car chaque pièce rapporte 5 points).
# On utilise l'opérateur * pour la multiplication et + pour l'addition.
# La fonction print() affiche le résultat à l'écran.
print(x * 1000 + y * 5)