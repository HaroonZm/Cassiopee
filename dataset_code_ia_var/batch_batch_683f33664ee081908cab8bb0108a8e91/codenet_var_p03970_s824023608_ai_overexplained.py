# Demande à l'utilisateur de saisir une chaîne de caractères au clavier
# La fonction input() attend que l'utilisateur entre du texte et appuie sur Entrée
s = input()

# Création d'une variable c contenant la chaîne de caractères 'CODEFESTIVAL2016'
# Cela crée une séquence ordonnée de caractères, où chaque caractère peut être accédé par son indice
c = "CODEFESTIVAL2016"

# Initialisation de la variable a à 0
# Cette variable servira à compter le nombre de différences entre les chaînes s et c
a = 0

# La fonction range(len(c)) crée un objet de type range débutant à 0 et allant jusqu'à la longueur de c (non inclus)
# len(c) retourne le nombre de caractères dans la chaîne c
# On va donc boucler sur tous les indices valides de la chaîne c, c'est-à-dire de 0 jusqu'à len(c)-1
for i in range(len(c)):
    # On compare le i-ème caractère de la chaîne s avec celui de la chaîne c
    # Si les deux caractères sont différents, l'expression s[i] != c[i] est vraie
    if s[i] != c[i]:
        # Si la condition expliquée ci-dessus est vérifiée, on incrémente la variable de compteur a de 1
        # L'opération a = a + 1 signifie qu'on augmente la valeur de a d'une unité
        a = a + 1

# Affiche la valeur finale de la variable a
# La fonction print() affiche à l'écran la valeur spécifiée entre parenthèses
print(a)