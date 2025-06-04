# Initialisation d'un dictionnaire vide nommé 'result'
# Ce dictionnaire va servir à stocker des couples (num, accepted)
result = {}

# Boucle infinie, qui sera interrompue lorsqu'une certaine condition sera remplie
while True:
    # Lecture d'une ligne au clavier, séparée par une virgule, puis conversion en entier
    # La fonction raw_input() lit l'entrée utilisateur sous forme de chaîne de caractères
    # La méthode split(',') découpe la chaîne en liste selon le séparateur virgule
    # La fonction map(int, ...) applique la conversion en entier sur chaque morceau
    num, accepted = map(int, raw_input().split(','))

    # Si les deux valeurs saisies valent 0, cela signifie que nous devons quitter la boucle
    if num == 0 and accepted == 0: 
        break  # Sortie de la boucle
    else:
        # Sinon, on place la valeur 'accepted' à la clé 'num' dans le dictionnaire 'result'
        result[num] = accepted

# Initialisation d'une variable appelée 'rank' à 1
# Ceci représentera le rang dans un classement
rank = 1

# Initialisation d'une variable 'accepted' à 0
# Cette variable va servir à se souvenir du nombre d'acceptations précédent dans la boucle suivante
accepted = 0      

# Boucle sur les éléments triés du dictionnaire 'result'
# La méthode result.items() retourne une liste des paires (clé, valeur)
# sorted() trie cette liste en utilisant la valeur (indice 1 du tuple x)
# L'option reverse=True trie dans l'ordre décroissant
for k, v in sorted(result.items(), key=lambda x: x[1], reverse=True):
    # Si la variable 'accepted' précédente est strictement supérieure à la valeur courante 'v'
    if accepted > v:
        # Cela signifie que le nombre d'acceptations a diminué, donc on incrémente le rang
        rank += 1
    # On associe la clé courante 'k' avec le rang actuel dans le dictionnaire 'result'
    result[k] = rank
    # On met à jour la variable 'accepted' avec la valeur actuelle 'v'
    accepted = v
        
# Nouvelle boucle infinie pour des requêtes utilisateur
while True:
    try:
        # On tente de lire une entrée utilisateur grâce à raw_input()
        # On convertit l'entrée saisie en entier
        num = int(raw_input())
        # On affiche le rang correspondant à la clé 'num' dans le dictionnaire 'result'
        print result[num]
    # Si la fin du fichier (EOF) est atteinte, une exception EOFError est levée
    except EOFError:
        # On sort alors proprement de la boucle
        break