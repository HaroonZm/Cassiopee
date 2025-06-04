# Demande à l'utilisateur de saisir une valeur
# La fonction input() affiche une invite (vide ici) et récupère ce que l'utilisateur tape au clavier sous forme de chaîne de caractères (str)
# La fonction int() convertit la chaîne de caractères obtenue en un entier (int)
s = int(input())

# Calcule le quotient de la division entière de s par 30
# L'opérateur // effectue une division entière, c'est-à-dire qu'il donne le nombre de fois que 30 rentre totalement dans s, en ignorant la partie décimale
quotient = s // 30

# Calcule le reste de la division de s par 30
# L'opérateur % (modulo) donne le reste de la division entière de s par 30, c'est-à-dire la partie de s qui reste après avoir retiré tous les multiples de 30
reste = s % 30

# Multiplie le reste obtenu par 2
# Cela double la valeur du reste
deux_fois_reste = 2 * reste

# Affiche les deux résultats sur une seule ligne, séparés par un espace par défaut grâce à la virgule dans print()
# Le premier affiché est le quotient (nombre entier de fois que 30 rentre dans s)
# Le second est le double du reste
print(quotient, deux_fois_reste)