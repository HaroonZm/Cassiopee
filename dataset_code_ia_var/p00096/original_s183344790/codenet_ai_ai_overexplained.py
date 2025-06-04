import sys  # Importe le module sys qui permet d’accéder à des objets utilisés ou maintenus par l’interpréteur Python (comme sys.stdin pour l’entrée standard)

# Création d’une liste appelée 'a' qui servira à stocker des entiers.
# L’opérateur '*' ici duplique la liste [0] 4001 fois, créant ainsi une liste de 4001 zéros.
a = [0] * 4001

# Début d’une boucle for allant de 0 jusqu’à 2000 inclus (car range(2001) va de 0 à 2000).
for i in range(2001):
    # Calcul de a[i]. On remplit aussi a[4000-i] avec la même valeur (symétrie dans la liste).
    
    # - (i + 3) calcule la valeur de i plus 3.
    # - -~i est l’opérateur « bitwise not » en Python, qui pour un nombre n retourne -(n+1). Mais dans ce code, il utilise -~i pour obtenir i+1 (un idiome pour incrémenter).
    # - -~-~i est l’équivalent de i+2 (en faisant deux fois le bitwise not).
    # - -~i est donc i+1.
    # L’expression (i+3) * (i+2) * (i+1) multiplie ces trois nombres entre eux.
    # La division entière (//) par 6 est utilisée.
    # Cette partie calcule le nombre de façons de choisir 3 éléments dans un ensemble de (i+3) éléments : c’est une combinaison C(i+3,3).
    
    # Ensuite, on vérifie si i > 999, c’est-à-dire i >= 1000.
    # Si c’est le cas, on soustrait a[i-1001] * 4 à la valeur précédente, sinon on soustrait 0.
    # Le booléen (i > 999) sera évalué à True ou False. En Python, True vaut 1 et False vaut 0.
    # Donc, a[i - 1001] * 4 * (i > 999) soustrait 4 * a[i - 1001] si i > 999, sinon 0.
    
    value = ((i + 3) * -~-~i * -~i) // 6 - a[i - 1001] * 4 * (i > 999)
    
    # Attribue la valeur calculée à la case i de la liste a.
    a[i] = value
    
    # Attribue la même valeur symétriquement à l’indice 4000 - i dans la liste a.
    # Cela signifie que la liste a est symétrique par rapport à son centre.
    a[4000 - i] = value

# Boucle sur chaque ligne de l’entrée standard (sys.stdin permet de lire ligne par ligne la saisie ou un fichier donné en entrée).
for e in sys.stdin:
    # 'e' contient une chaîne correspondant à une ligne de l’entrée standard (avec souvent un '\n' à la fin).
    # int(e) convertit la chaîne de caractères en un entier.
    # On accède alors à la valeur correspondante dans la liste a.
    # Enfin, on imprime cette valeur (affichée sur la sortie standard, généralement l’écran).
    print(a[int(e)])