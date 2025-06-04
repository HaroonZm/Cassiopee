# Définition d'une fonction nommée 'check' qui prend un argument 'num'
def check(num):
    # Vérifie si le paramètre 'num' est une chaîne vide
    # Si c'est le cas, retourne False car une chaîne vide n'est pas un nombre valide
    if num == "":
        return False
    # Vérifie si le premier caractère de 'num' est le caractère "0"
    if num[0] == "0":
        # Si la chaîne est exactement "0", retourne True (c'est un cas valide)
        # Sinon, retourne False pour prévenir les zéros en tête (par exemple "01")
        return num == "0"
    # Convertit la chaîne 'num' en entier avec int(num) et vérifie qu'il est dans la plage 0 à 255 (inclus)
    # Retourne True si tel est le cas, False sinon
    return 0 <= int(num) <= 255

# Lit une ligne de texte de l'entrée standard (typiquement le clavier)
# La fonction input() retourne une chaîne de caractères saisie par l'utilisateur
s = input()

# Initialise une variable nommée 'ans' à 0 pour compter le nombre de solutions valides trouvées
ans = 0

# Boucle for qui initialise la variable i à 1 et l'incrémente jusqu'à 3 (non inclus), c'est-à-dire i = 1, 2, 3
for i in range(1, 4):
    # Boucle for imbriquée pour j de 1 à 3 inclus (j prend les valeurs 1, 2, 3)
    for j in range(1, 4):
        # Boucle for imbriquée pour k de 1 à 3 inclus (k prend les valeurs 1, 2, 3)
        for k in range(1, 4):
            # Découpe la chaîne 's' en quatre parties :
            # n1 contient les caractères de l'indice 0 (inclus) à i (exclu)
            n1 = s[:i]
            # n2 contient les caractères de l'indice i (inclus) à i+j (exclu)
            n2 = s[i:i+j]
            # n3 contient les caractères de l'indice i+j (inclus) à i+j+k (exclu)
            n3 = s[i+j:i+j+k]
            # n4 contient les caractères de l'indice i+j+k jusqu'à la fin de la chaîne (slice sans bornes supérieure)
            n4 = s[i+j+k:]
            # Vérifie si toutes les parties n1, n2, n3 et n4 sont valides avec la fonction 'check'
            # L'opérateur 'and' retourne True seulement si toutes les conditions sont vraies
            if check(n1) and check(n2) and check(n3) and check(n4):
                # Si les quatre segments sont valides, incrémente 'ans' de 1
                ans += 1

# Affiche la valeur finale de 'ans' sur la sortie standard (l'écran)
print(ans)