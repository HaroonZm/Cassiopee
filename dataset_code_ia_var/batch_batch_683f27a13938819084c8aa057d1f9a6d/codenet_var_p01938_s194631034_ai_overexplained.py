# Demande à l'utilisateur de saisir une chaîne de caractères (str), stockée dans la variable S
S = input()

# Initialise deux variables :
# cnt : compteur, mis à 0 au départ. Servira à compter un certain nombre d'événements.
# x : initialise à 65, qui correspond au code ASCII (American Standard Code for Information Interchange)
# du caractère 'A'. Le code ASCII d'un caractère est obtenu par la fonction ord().
cnt = 0  # Compteur initialisé à zéro
x = 65   # Code ASCII du caractère 'A'

# Parcours, caractère par caractère, la chaîne de caractères S,
# c prend la valeur de chaque caractère dans l'ordre de la chaîne.
for c in S:
    # Calcule le code ASCII du caractère courant c avec ord(c)
    # Vérifie si la valeur de x est supérieure ou égale (>=) à ce code ASCII.
    # En Python, la comparaison x >= ord(c) va retourner True (si vrai) ou False (si faux).
    # En contexte numérique, True est équivalent à 1 et False à 0.
    # On ajoute donc à cnt 1 si x >= ord(c), 0 sinon.
    cnt = cnt + (x >= ord(c))

    # Met à jour la valeur de x pour la prochaine itération.
    # x devient le code ASCII du caractère courant c.
    x = ord(c)

# Après la boucle, affiche la valeur finale de cnt (imprime le compteur calculé)
print(cnt)