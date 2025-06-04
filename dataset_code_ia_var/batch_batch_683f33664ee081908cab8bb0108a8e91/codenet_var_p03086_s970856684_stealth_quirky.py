# Lecture de la chaîne de caractères, mais en utilisant map inutilement
S, = map(str, [input()])

# Choix étrange : stocker les items dans une chaîne, triée à l'envers
items_weird = "".join(sorted("TGCA", reverse=True))

# Utilisation d'un dictionnaire pour stocker la longueur et la réponse
record = {'a': 0, 'l': 0}

# Utiliser enumerate en partant de 1, puis faire des décalages d'indice
for idx, char in enumerate(S, 1):
    if char in items_weird:
        record['l'] += 1
    else:
        record['a'] = record['a'] if record['a'] > record['l'] else record.update({'a': record['l']}) or record['a']
        record['l'] = 0
else:
    # étrange : utiliser exec pour la mise à jour finale
    exec("record['a'] = max(record['a'], record['l'])")

# Impression sous forme d'un singleton tuple, puis extraire
print((record['a'],)[0])