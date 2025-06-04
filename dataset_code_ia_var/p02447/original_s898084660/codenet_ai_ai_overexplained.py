# Demande à l'utilisateur de saisir une valeur depuis le clavier (au format texte)
# La fonction input() affiche une invite de saisie et retourne la chaîne de caractères tapée par l'utilisateur
# La fonction int() convertit la chaîne de caractères obtenue en un entier
n = int(input())

# Création d'une liste vide qui sera utilisée pour stocker plusieurs éléments
# Une liste est une collection d'éléments ré-ordonnables et modifiables
li = []

# Boucle for utilisant la fonction range() pour itérer n fois
# range(n) génère une séquence de nombres de 0 à n-1 inclus
for i in range(n):
    # Lecture d'une ligne de texte tapée par l'utilisateur
    # input() retourne une chaîne de caractères, généralement les éléments sont séparés par des espaces
    # La méthode split() divise la chaîne de caractères selon les espaces et retourne une liste de chaînes
    # map(int, ...) applique la fonction int() à chaque chaîne découpée, ce qui les convertit en entiers
    # list(...) convertit l'objet map en liste, ce qui donne une liste d'entiers
    l = list(map(int, input().split()))
    # Ajout de la liste d'entiers obtenue à la liste principale 'li'
    # append() ajoute l'élément spécifié à la fin de la liste existante
    li.append(l)

# Trie la liste 'li' contenant des listes d'entiers
# sorted(...) retourne une nouvelle liste triée, sans modifier l'originale, selon l'ordre croissant
# Pour des listes imbriquées, le tri se fait d'abord sur le premier élément, puis sur le second, etc.
li = sorted(li)

# Boucle for qui parcourt chaque élément dans la liste 'li'
# Ici, chaque élément 'i' est lui-même une liste d'entiers
for i in li:
    # map(str, i) convertit chaque entier de la liste en une chaîne de caractères
    # " ".join(...) fusionne toutes ces chaînes de caractères en une seule, en insérant un espace entre chaque
    # print(...) affiche la chaîne finale à l'écran et passe à la ligne suivante automatiquement
    print(" ".join(map(str, i)))