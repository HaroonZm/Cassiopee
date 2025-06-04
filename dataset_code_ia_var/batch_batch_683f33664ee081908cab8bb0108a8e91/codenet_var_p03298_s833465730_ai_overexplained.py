# Demande à l'utilisateur de saisir un entier depuis l'entrée standard (clavier)
# int() convertit la chaîne lue en nombre entier (base 10).
n = int(input())

# Demande à l'utilisateur une chaîne de caractères composée de symboles (caractères)
# list() transforme la chaîne en une liste de caractères pour l'accès indexé.
s = list(input())

# Prend les n premiers caractères de la liste s et les stocke dans 'l'
# s[:n] signifie "tous les éléments de s, depuis l'indice 0 jusqu'à mais non inclus n"
l = s[:n]

# Prend les n caractères suivants (de la position n à la fin de s), puis inverse leur ordre à l'aide de [::-1]
r = s[n:][::-1]

# Crée un dictionnaire vide nommé 'd' qui va stocker des paires (chaînes, chaînes) comme clés, et des entiers comme valeurs (compteurs)
d = {}

# Crée un autre dictionnaire vide nommé 'e', ayant le même but que 'd' mais pour les sous-chaînes inversées
e = {}

# Boucle sur tous les entiers i compris entre 0 et 2^n - 1 (soit 1<<n possibilités).
# "1 << n" équivaut à 2 puissance n, car << est l'opérateur de décalage binaire à gauche.
for i in range(1 << n):
    # Initialise quatre chaînes vides: s, t, u, v
    # Ces chaînes serviront à accumuler différents caractères à chaque itération
    s = ''
    t = ''
    u = ''
    v = ''

    # Pour chaque position j parmi les n positions (de 0 à n-1)
    for j in range(n):
        # (i >> j) & 1 extrait le j-ième bit de i (compris comme un masque de sélection)
        # Si ce bit est à 1, la condition est vraie, sinon fausse.
        if (i >> j) & 1:
            # Ajoute le j-ième caractère de 'l' à la chaîne s
            s += l[j]
            # Ajoute le j-ième caractère de 'r' à la chaîne t
            t += r[j]
        else:
            # Sinon, ajoute le j-ième caractère de 'l' à la chaîne u
            u += l[j]
            # Ajoute le j-ième caractère de 'r' à la chaîne v
            v += r[j]

    # On utilise le couple (s, u) comme clé dans le dictionnaire 'd'
    # Si cette clé existe déjà, incrémente sa valeur, sinon utilise 0 comme valeur par défaut grâce à la méthode get()
    d[(s, u)] = d.get((s, u), 0) + 1

    # On fait de même pour (t, v) dans le dictionnaire 'e'
    e[(t, v)] = e.get((t, v), 0) + 1

# Initialise un compteur à zéro; il servira à compter le nombre final recherché
a = 0

# Parcourt toutes les clés du dictionnaire 'd'
for i in d.keys():
    # Ajoute à 'a' le produit du nombre d'occurrences de la clé dans 'd' par le nombre d'occurrences de cette clé dans 'e'
    # La méthode get(i,0) retourne 0 si la clé n'est pas présente dans 'e'
    a += d[i] * e.get(i, 0)

# Affiche le résultat final à l'écran (le nombre total calculé)
print(a)