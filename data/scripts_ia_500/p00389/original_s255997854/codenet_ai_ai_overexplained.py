# Demande à l'utilisateur d'entrer deux nombres entiers séparés par un espace
# La fonction input() récupère la chaîne de caractères entrée par l'utilisateur
# La méthode split() divise cette chaîne en une liste de sous-chaînes en utilisant l'espace comme séparateur
# La fonction map applique la fonction int à chaque élément de cette liste pour convertir les chaînes en entiers
# Les deux valeurs entières obtenues sont assignées aux variables n et k respectivement
n, k = map(int, input().split())

# Initialise la variable weight à 1
# Cette variable représente une quantité initiale ou un poids de départ dans le contexte du problème
weight = 1

# Initialise la variable rest avec la valeur de n moins 1
# Cette variable représente la quantité restante à traiter ou à distribuer après avoir pris en compte le poids initial
rest = n - 1

# Initialise la variable layers à 1
# Cette variable compte le nombre de "couches" ou d'étapes effectuées, commence à 1 car on a déjà une couche initiale
layers = 1

# Boucle infinie qui sera interrompue explicitement avec un break quand une condition sera remplie
# Cette boucle sert à itérer tant que certaines conditions sont satisfaites, modifiant weight, rest et layers à chaque tour
while True:
    # Calcule la valeur 'add' qui correspond au nombre d'éléments à ajouter
    # weight // k est la division entière de weight par k, donnant le quotient sans la partie décimale
    # weight % k est le reste de la division de weight par k
    # bool(weight % k) convertit ce reste en un booléen: True (1) si le reste est différent de zéro, sinon False (0)
    # La somme weight // k + bool(weight % k) arrondit ainsi à l'entier supérieur sans utiliser ceil()
    add = weight // k + bool(weight % k)

    # Vérifie si la quantité à ajouter 'add' est inférieure ou égale à la quantité restante 'rest'
    # Si c'est le cas, on peut effectuer l'ajout et continuer la boucle
    if add <= rest:
        # Soustrait 'add' de 'rest' pour mettre à jour la quantité restante
        rest -= add

        # Augmente 'weight' de la valeur 'add', simulant le fait d'ajouter cette quantité au poids actuel
        weight += add

        # Incrémente le compteur 'layers' de 1, puisqu'on a ajouté une nouvelle couche ou étape
        layers += 1
    else:
        # Si 'add' est plus grand que 'rest', on ne peut pas continuer à ajouter
        # On interrompt la boucle infinie avec le mot-clé break
        break

# Affiche le nombre total de couches calculées
# La fonction print() convertit automatiquement la variable layers en chaîne de caractères pour l'affichage
print(layers)