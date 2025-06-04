# Initialisation d'une liste vide pour stocker les résultats finaux
ans = []

# Boucle infinie qui sera interrompue manuellement avec 'break'
while True:
    # Lecture d'une entrée utilisateur sous forme de chaîne de caractères
    n = input()        # Demande à l'utilisateur de saisir une valeur

    # Vérification si la valeur saisie est égale à 0 (test d'arrêt)
    # Comme input() retourne du texte et non un nombre, il faudrait le convertir en int pour la comparaison,
    # mais dans le code d'origine, comparé directement à 0 fonctionne seulement en Python 2 avec input()
    if n == 0:
        # Arrêter la boucle si l'entrée est 0
        break

    # Initialisation d'un compteur qui commence à 1
    c = 1

    # Calcul du carré de n, ce qui donne le nombre total de cellules à remplir dans le "cercle"
    N = n * n

    # Création d'une liste de taille N, remplie de zéros, représentant le "cercle"
    circle = [0] * N  # Les cases à remplir seront modifiées plus tard

    # Calcul de la position initiale (p). 
    # (N + 1) / 2 - 1 place le point de départ au centre
    # En python 2, / est la division entière par défaut pour les entiers, mais ici ça fonctionne grâce à input()
    p = (N + 1) / 2 - 1

    # Boucle pour remplir tous les nombres de 1 à N dans la liste 'circle'
    while c <= N:
        # Premier test : si p atteint la fin du cercle, le remettre à 1
        if p == N:
            p = 1
        # Deuxième test : si la position actuelle est un multiple de n
        elif p % n == 0:
            # Passer à la position suivante
            p += 1
        # Troisième test : si le déplacement de n dépasse la longueur du cercle
        elif p + n > N:
            # Revenir en arrière avec un calcul pour repositionner correctement p
            p -= (N - n - 1)
        else:
            # Dans le cas général, avancer de n+1 positions dans le cercle
            p += n + 1

        # Vérifie si la position cible dans circle est déjà occupée
        if circle[p - 1] != 0:
            # Tant que la position est occupée, trouver une place libre selon des règles précises
            while circle[p - 1] != 0:
                # Si on est à une certaine position critique en bas du cercle
                if p == N - n + 1:
                    # Revenir au début de la ligne suivante
                    p = n
                # Si p-1 est un multiple de n, donc à la fin d'une ligne
                elif (p - 1) % n == 0:
                    # Sauter de deux lignes moins une case
                    p += (n * 2 - 1)
                # Si le déplacement de n atteint ou dépasse la fin
                elif p + n > N:
                    # Retour en arrière à un point de départ spécifique
                    p -= N - n + 1
                else:
                    # Avancer de n-1 positions
                    p += n - 1

        # Remplir la position trouvée avec la valeur c
        circle[p - 1] = c

        # Incrémenter c pour la prochaine valeur à placer dans le cercle
        c += 1

    # Réinitialisation de la variable p à 0 pour l'affichage qui va suivre
    p = 0
    # Initialisation d'une chaîne temporaire pour construire la représentation finale des lignes
    temp = ''

    # On construit les lignes, une à une, pour former la sortie sous forme de carré
    while p * n != N:
        # Sélectionne une tranche de la liste 'circle' correspondant à une ligne
        # map applique la fonction lambda à chaque élément de la tranche :
        # - conversion en chaîne
        # - alignement à droite sur 4 caractères à l'aide de rjust(4)
        temp += ''.join(map(lambda x: str(x).rjust(4), circle[n * p:n * (p + 1)]))
        # Ajoute un saut de ligne à la fin de chaque ligne affichée
        temp += '\n'
        # Incrémente le numéro de ligne
        p += 1

    # Retire d'éventuels sauts de ligne finaux superflus avec rstrip()
    # Ajoute la représentation finale à la liste des réponses
    ans.append(temp.rstrip())

# Parcourt chaque élément de la liste 'ans'
for i in ans:
    # Affiche chaque bloc formaté de nombres à la sortie standard
    print i   # En python 2, print est une instruction, pas une fonction. Pour python 3, il faudrait print(i)