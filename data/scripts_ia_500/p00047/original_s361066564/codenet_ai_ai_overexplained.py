# Initialisation d'une liste appelée 'balls' contenant trois éléments entiers
# La liste représente trois balles, chaque élément vaut 1 ou 0
# Ici, la première balle est 1 (présente), les deux autres sont 0 (absentes)
balls = [1,0,0]

# Démarrage d'une boucle infinie
# La boucle se répète indéfiniment jusqu'à ce qu'une instruction 'break' soit rencontrée
while 1:
    # Bloc try pour tenter d'exécuter un code qui peut potentiellement générer une erreur
    try:
        # Lecture d'une ligne depuis l'entrée standard (l'utilisateur tape quelque chose)
        # La chaîne de caractères saisie est supposée contenir deux lettres séparées par une virgule
        # La méthode 'split' avec le séparateur ',' divise cette chaîne en deux sous-chaînes
        # Ces deux sous-chaînes sont affectées respectivement aux variables 'a' et 'b'
        a,b = input().split(',')
        
        # Conversion de la lettre a en un indice numérique
        # ord() donne le code ASCII (entier) correspondant à un caractère
        # ord('A') est la valeur ASCII de la lettre 'A'
        # en soustrayant ord('A'), on transforme la lettre en un index de 0 à 25, avec 'A' -> 0, 'B' -> 1, etc.
        i1 = ord(a) - ord("A")
        
        # Conversion similaire pour la lettre b
        i2 = ord(b) - ord("A")
        
        # Échange (swap) des valeurs des éléments dans la liste 'balls' aux indices i1 et i2
        # Cela signifie que la position des balles est modifiée en fonction des lettres saisies
        balls[i1],balls[i2] = balls[i2],balls[i1]
    
    # Bloc except qui intercepte toutes les exceptions (erreurs) pouvant survenir dans le bloc try
    # Ici, cela sert à sortir de la boucle lorsqu'une erreur survient, par exemple quand l'entrée n'est pas au bon format
    except:
        # Sortie immédiate de la boucle infinie
        break

# Parcours des indices de 0 à 2 (inclus)
for i in range(0,3):
    # Vérification si la valeur dans balls à l'indice i vaut 1 (vrai)
    # Cela signifie que la balle est présente à cette position
    if balls[i]:
        # Conversion de l'indice i en lettre correspondante ('A' pour 0, 'B' pour 1, 'C' pour 2)
        # ord('A') + i calcule le code ASCII de la lettre correspondante
        # chr() convertit ce code ASCII en caractère
        # Impression de ce caractère, indiquant la position où la balle est présente
        print(chr(i + ord("A")))