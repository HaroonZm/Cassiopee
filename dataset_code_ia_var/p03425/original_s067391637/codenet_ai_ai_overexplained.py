# Demander à l'utilisateur d'entrer un nombre entier via l'entrée standard (input())
# La fonction int() convertit la chaîne d'entrée en un entier
n = int(input())

# Créer une liste contenant les lettres 'M', 'A', 'R', 'C' et 'H'
# Ces lettres représentent les initiales que nous voulons suivre
marchSentence = ["M", "A", "R", "C", "H"]

# Initialiser une liste de cinq zéros, chacun correspondant à un compteur pour une des lettres ci-dessus
marchCount = [0, 0, 0, 0, 0]

# Initialiser une variable pour garder la somme finale du résultat
marchSum = 0

# Boucle for qui itère exactement n fois, où n est le nombre donné par l'utilisateur
for i in range(n):
    # Lire une chaîne via input() représentant le nom ou mot entré par l'utilisateur
    s = input()
    # Extraire la première lettre de cette chaîne
    sa = s[0]
    # Vérifier si cette lettre figure dans la liste marchSentence
    # .count() renverra 1 si c'est le cas, 0 sinon
    if marchSentence.count(sa) > 0:
        # Obtenir la position (index) de cette lettre dans la liste marchSentence
        num = marchSentence.index(s[0])
        # Vérifier que l'index trouvé n'est pas -1 (même si list.index lancerait une exception si l'élément n'est pas trouvé)
        if num > -1:
            # Incrémenter le compteur correspondant dans marchCount
            marchCount[num] += 1

# Les trois boucles for suivantes servent à parcourir toutes les combinaisons de trois lettres distinctes prises parmi les cinq possibles
# Cela revient à énumérer toutes les combinaisons (sans répétition et sans ordre) de 3 éléments parmi 5

# Première boucle for : a varie de 0 à 2 inclus (0, 1, 2)
for a in range(0, 3):
    # Deuxième boucle for : b varie de a+1 à 3 inclus (dépend du a courant)
    for b in range(a + 1, 4):
        # Troisième boucle for : c varie de b+1 à 4 inclus (dépend du b courant)
        for c in range(b + 1, 5):
            # Multiplie le nombre de mots (comptes) pour chaque lettre du triplet courant
            # Additionne le produit au résultat total marchSum
            marchSum += marchCount[a] * marchCount[b] * marchCount[c]

# Après avoir parcouru toutes les combinaisons, afficher la somme totale trouvée
print(marchSum)