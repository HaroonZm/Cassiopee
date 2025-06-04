# Demande à l'utilisateur de saisir une valeur, généralement censée être un nombre indiquant combien d'éléments vont suivre
n = input()  # Ici, la valeur saisie par l'utilisateur est stockée dans la variable n sous forme de chaîne de caractères (string)

# Demande à l'utilisateur de saisir une ligne de texte, puis retire les espaces de début et fin grâce à strip()
# Ensuite, split(" ") découpe la chaîne selon les espaces simples (" "), créant une liste de mots ou nombres au format string
s = input().strip().split(" ")
# Par exemple, si l'utilisateur tape : "1 2 3", alors s vaudra ["1", "2", "3"]

# Demande à l'utilisateur un nombre, le lit, enlève les espaces éventuels au début/fin, et convertit la string reçue en un entier (int)
q = int(input().strip())

# Demande à l'utilisateur une nouvelle ligne, retire les espaces en trop, découpe la chaîne, et stocke la liste résultante dans t
t = input().strip().split(" ")
# Par exemple, si l'utilisateur tape : "2 4 5", t vaudra ["2", "4", "5"]

# Initialise un compteur, dont le but sera de compter combien d'éléments de la liste t sont présents dans la liste s
count = 0

# Pour chaque élément i contenu dans la liste t (on parcourt donc tous les éléments de t un par un)
for i in t:
    # On vérifie si cet élément i est présent dans la liste s.
    # L'opérateur "in" vérifie si i existe dans s (c'est un test d'appartenance)
    if i in s:
        # Si c'est le cas (donc si i apparaît dans s), on ajoute 1 au compteur count (c'est une incrémentation)
        count += 1

# Affiche la valeur finale de count, c'est-à-dire le nombre d'éléments de t présents dans s
print(count)