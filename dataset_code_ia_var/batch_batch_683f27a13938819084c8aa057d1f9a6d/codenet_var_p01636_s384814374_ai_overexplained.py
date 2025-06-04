# Demande à l'utilisateur de saisir une chaîne de caractères au clavier
s = raw_input()

# Initialise une variable ans à 0.
# Cette variable va servir à compter le nombre de résultats qui satisfont les conditions du problème.
ans = 0

# Lance une boucle for qui va parcourir tous les indices possibles de la chaîne 's'
# range(len(s)) crée une séquence de nombres allant de 0 à la longueur de s - 1 (soit tous les indices valides de s)
for i in range(len(s)):
    # Le but de ce bloc est d'ignorer certains cas particuliers.
    # Si le caractère à l'indice i est "0" (le chiffre zéro)
    # et si i n'est pas le dernier indice de la chaîne (c'est-à-dire pas à la fin de la chaîne)
    if s[i] == "0" and i != len(s) - 1:
        # continue signifie ignorer le reste de cette itération de la boucle et passer à la suivante
        continue

    # Cette étape consiste à séparer la chaîne en deux parties à l'indice i
    # la partie gauche étant les caractères avant l'indice i (exclu)
    # Si i n'est pas zéro, 's[:i]' prend la sous-chaîne du début jusqu'à i (non inclus)
    # On convertit cette sous-chaîne en entier avec int() pour pouvoir faire des comparaisons numériques plus tard
    # Si i est zéro (donc pas de caractères à gauche), on met directement la valeur 0 pour 'left'
    left = int(s[:i]) if i else 0

    # La partie droite commence à i (inclus) et va jusqu'à la fin de la chaîne
    # On convertit aussi cette sous-chaîne en entier pour les mêmes raisons
    right = int(s[i:])

    # Vérifie deux conditions :
    # 1) 'left' est inférieur ou égal à 'right'
    # 2) 'left' et 'right' sont tous deux pairs ou tous deux impairs (c'est-à-dire que leurs restes modulo 2 sont identiques)
    if left <= right and left % 2 == right % 2:
        # Si la condition est vraie, on incrémente de 1 la variable 'ans'
        ans += 1

# Affiche la valeur finale de la variable 'ans'
print ans