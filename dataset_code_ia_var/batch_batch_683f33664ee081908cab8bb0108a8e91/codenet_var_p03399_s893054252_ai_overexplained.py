# Création d'une liste vide qui servira à stocker les valeurs saisies par l'utilisateur
# Une liste est une structure de données ordonnée et mutable en Python, on l'initialise avec []
list = []

# Boucle for qui va répéter 4 fois l'ensemble des instructions indentées qui suivent
# range(4) génère une séquence de nombres de 0 à 3 inclus (4 éléments)
for i in range(4):
    # input() affiche une invite à l'utilisateur et récupère une saisie clavier sous forme de chaîne (str)
    # int() convertit la saisie de l'utilisateur qui est une chaîne de texte (str) en un nombre entier (int)
    # append() ajoute cet entier à la fin de la liste définie précédemment
    list.append(int(input()))

# Création d'une nouvelle liste appelée 'train'
# Cette liste est constituée du premier élément [indice 0] et du deuxième élément [indice 1] de la liste principale
train = [list[0], list[1]]

# Création d'une nouvelle liste appelée 'bus'
# Cette liste contient le troisième [indice 2] et le quatrième élément [indice 3] de la liste principale
bus = [list[2], list[3]]

# La fonction min() retourne la plus petite valeur d'une séquence ou liste passée en argument
# On calcule min(train) pour obtenir la plus petite valeur de la liste train
# On calcule min(bus) pour obtenir la plus petite valeur de la liste bus
# On additionne ces deux valeurs grâce à l'opérateur +
# La fonction print() affiche le résultat à l'écran sous forme de texte
print(min(train) + min(bus))