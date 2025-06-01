# Le dictionnaire COLOR associe des codes hexadécimaux de couleur (sous forme de chaînes de caractères) à leurs noms anglais correspondants.
# Chaque clé est une chaîne représentant une couleur sous forme RGB en hexadécimal sur 6 chiffres, en minuscules,
# par exemple "000000" pour le noir, et chaque valeur est le nom anglais correspondant à cette couleur.
COLOR = {
    "000000": "black",    # Noir (absence totale de lumière)
    "0000ff": "blue",     # Bleu (maximum sur le canal bleu)
    "00ff00": "lime",     # Vert vif (maximum sur le canal vert)
    "00ffff": "aqua",     # Cyan (maximum sur vert et bleu)
    "ff0000": "red",      # Rouge (maximum sur le canal rouge)
    "ff00ff": "fuchsia",  # Magenta (maximum sur rouge et bleu)
    "ffff00": "yellow",   # Jaune (maximum sur rouge et vert)
    "ffffff": "white"     # Blanc (maximum sur tous les canaux)
}

# Début d'une boucle infinie afin de traiter plusieurs entrées utilisateur jusqu'à ce qu'une condition d'arrêt soit remplie.
while True:
    # Lecture d'une ligne depuis l'entrée standard sous forme de chaîne de caractères, qui sera stockée dans la variable s.
    s = input()
    # Si la longueur de la chaîne s est égale à 1, cela signifie que l'entrée est une chaîne unique,
    # ce qui sert ici comme condition d'arrêt pour sortir de la boucle.
    if len(s) == 1:
        break  # Sortie immédiate de la boucle et donc fin de programme.

    # Initialisation de la variable color à une chaîne vide.
    # Cette variable servira à construire une nouvelle chaîne représentant une couleur rgb modifiée.
    color = ""

    # La fonction zip permet de regrouper deux séquences élément par élément, ici sur des slices de la chaîne s.
    # s[1::2] signifie 'prendre les éléments de la chaîne s, en partant de l'indice 1, tous les deux caractères'
    # donc s[1], s[3], s[5], ...
    # s[2::2] signifie 'prendre les éléments de la chaîne s, en partant de l'indice 2, tous les deux caractères'
    # donc s[2], s[4], s[6], ...
    # zip va ensuite combiner ces éléments par paire (first, second) en parallèle à chaque itération.
    for first, second in zip(s[1::2], s[2::2]):
        # Ici, first et second sont des caractères individuels représentant des chiffres hexadécimaux.
        # La concaténation first + second forme une chaîne de deux caractères représentant un octet hexadécimal (00 à ff).
        # int(..., 16) convertit cette chaîne hexadécimale en nombre entier base 10.
        # On compare ce nombre à 127 (la moitié de 255, 8-bit max) pour décider la luminosité de cette composante.
        if int(first + second, 16) <= 127:
            # Si la valeur décimale est inférieure ou égale à 127,
            # cela signifie une intensité considérée faible pour cette composante.
            # On ajoute alors "00" (zéro en hexadécimal) à la chaîne color, ce qui correspond à aucun signal pour cette composante.
            color += "00"
        else:
            # Sinon, si la valeur est supérieure à 127,
            # cela signifie une intensité forte pour cette composante.
            # On ajoute alors "ff" (maximum 255 en hexadécimal) pour ce canal.
            color += "ff"

    # Après la boucle, la variable color contient une chaîne hexadécimale RGB de six caractères (trois octets),
    # chaque paire représentant un canal (rouge, vert, bleu) à "00" ou "ff".
    # Cette chaîne est utilisée comme clé pour accéder au dictionnaire COLOR afin de récupérer le nom anglais
    # correspondant à la couleur approximative calculée.
    # Print affiche cette valeur à la sortie standard.
    print(COLOR[color])