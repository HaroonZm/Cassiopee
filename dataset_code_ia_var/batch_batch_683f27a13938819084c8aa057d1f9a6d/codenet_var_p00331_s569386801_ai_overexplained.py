# Demande une entrée utilisateur sous forme de chaîne de caractères, généralement tapée au clavier
# La méthode input() permet de récupérer cet input utilisateur
# La méthode split() divise la chaîne de caractères en une liste de sous-chaînes en utilisant l'espace comme séparateur par défaut
# La compréhension de liste [int(e) for e in input().split()] parcourt chaque élément 'e' de la liste obtenue par split()
# Chaque sous-chaîne 'e' est convertie en entier à l'aide de la fonction int()
# Après cette opération, on obtient une liste d'entiers que l'on stocke dans la variable nums
nums = [int(e) for e in input().split()]

# On récupère le premier élément de la liste 'nums' en utilisant l'index 0
# Cet élément est supposé représenter la valeur de 'h'
h = nums[0]

# On récupère le deuxième élément de la liste 'nums' en utilisant l'index 1
# Cet élément est supposé représenter la valeur de 'r'
r = nums[1]

# On additionne h et r afin d'obtenir leur somme
# La somme est stockée dans la variable 'k'
k = h + r

# On effectue un test conditionnel pour vérifier si la variable 'k' est supérieure ou égale à 1
if k >= 1:
    # Si la condition k >= 1 est vraie, alors on affiche la chaîne de caractères "1" à l'écran grâce à la fonction print()
    print("1")
# Sinon, on teste une seconde condition
elif k <= -1:
    # Si la variable 'k' est inférieure ou égale à -1, alors on affiche la chaîne de caractères "-1"
    print("-1")
# Enfin, si aucune des deux conditions précédentes n'est remplie,
# cela veut dire que k n'est ni supérieur ou égal à 1, ni inférieur ou égal à -1, donc obligatoirement k == 0
elif k == 0:
    # On affiche "0" dans ce cas particulier
    print("0")