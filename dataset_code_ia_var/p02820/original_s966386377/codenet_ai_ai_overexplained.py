# Lecture de deux entiers n et k à partir de l'entrée standard (input)
# La fonction input() lit une ligne de texte depuis l'entrée standard.
# La fonction split() divise cette ligne en morceaux (basés sur les espaces).
# La fonction map(int, ...) applique int à chaque morceau pour les convertir en entier.
n, k = map(int, input().split())

# Lecture de trois entiers R, S et P sur une autre ligne de l'entrée standard.
# Même processus que ci-dessus : lire la ligne, découper et convertir en entiers.
R, S, P = map(int, input().split())

# Lecture d'une chaîne de caractères t via input(), qui représente les coups de l'adversaire.
t = input()

# Initialisation d'une variable entière ans à 0. 
# Cette variable stockera le score total accumulé pendant le jeu.
ans = 0

# Initialisation d'une liste win vide.
# Cette liste contiendra, pour chaque coup de l'adversaire, le coup choisi pour gagner.
win = []

# Boucle for itérant sur chaque caractère tt de la chaîne t.
for tt in t:
    # Si le coup de l'adversaire est 'r' (pierre) :
    if tt == 'r':
        # Ajout de 'p' (papier) à la liste win, car le papier bat la pierre.
        win += 'p'
        # Ajout à ans du score associé à battre la pierre (P).
        ans += P
    # Si le coup de l'adversaire est 's' (ciseaux) :
    elif tt == 's':
        # Ajout de 'r' (pierre) à la liste win, car la pierre bat les ciseaux.
        win += 'r'
        # Ajout à ans du score associé à battre les ciseaux (R).
        ans += R
    # Si le coup de l'adversaire n'est ni 'r' ni 's', on suppose que c'est 'p' (papier) :
    else:
        # Ajout de 's' (ciseaux) à la liste win, car les ciseaux battent le papier.
        win += 's'
        # Ajout à ans du score associé à battre le papier (S).
        ans += S

# Début d'une boucle for sur i allant de 0 à k-1 (i.e., range(k)).
for i in range(k):
    # Construction d'une sous-liste l.
    # l commence à l'index i et prend ensuite chaque k-ème élément de la liste win.
    # win[i::k] signifie : partir de l, avancer de k à chaque fois.
    l = win[i::k]
    # Pour chaque index j de 1 à la longueur de l (exclus), c'est-à-dire à partir du deuxième élément de l :
    for j in range(1, len(l)):
        # Si le coup choisi à la position j est le même que celui à la position précédente (j-1) :
        if l[j] == l[j-1]:
            # On annule le score de ce coup car on ne peut pas jouer deux fois le même coup consécutivement dans la même série modulo k.
            if l[j] == 'p':
                ans -= P  # On enlève le score du papier
            elif l[j] == 'r':
                ans -= R  # On enlève le score de la pierre
            else:
                ans -= S  # On enlève le score des ciseaux
            # Enfin, on remplace ce coup par 'z' (un caractère impossible lors du jeu) pour éviter de pénaliser à nouveau lors d'autres vérifications.
            l[j] = 'z'

# Affichage du score total calculé.
print(ans)