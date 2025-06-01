# Définition d'une liste contenant les types de groupes sanguins
l = ["A", "B", "AB", "O"]  # Cette liste sera utilisée pour itérer dans un ordre défini

# Création d'un dictionnaire pour stocker un compteur initialisé à 0 pour chaque groupe sanguin
# Un dictionnaire en Python est une structure de données clé-valeur qui permet de stocker et récupérer des données rapidement
dict = {"A": 0, "B": 0, "AB": 0, "O": 0}  # Ici, chaque type de groupe sanguin est une clé et la valeur est le compteur initialisé à 0

# Démarrage d'une boucle infinie pour lire plusieurs lignes d'entrée utilisateur
while True:
    try:
        # Lecture d'une ligne au format "nombre, groupe_sanguin"
        # La méthode input() attend une saisie utilisateur jusqu'à ce qu'on appuie sur Entrée
        # La méthode split(",") divise la chaîne en deux parties autour de la virgule, 
        # retournant une liste de deux éléments: n et s
        n, s = input().split(",")
    except:
        # Si une erreur survient lors du split (par exemple plus ou moins d'éléments) ou à la fin de l'entrée,
        # on sort de la boucle infinie avec break
        break
    
    # Incrémentation du compteur dans le dictionnaire pour la clé correspondant au groupe sanguin s
    # Le groupe sanguin est la chaîne juste après la virgule dans l'entrée utilisateur
    dict[s] += 1  # On ajoute 1 au compteur existant pour ce groupe sanguin

# Parcours de la liste l qui contient les groupes sanguins dans un ordre spécifique
for i in l:
    # Affichage du compteur pour chaque groupe sanguin
    # print() envoie la valeur sur la sortie standard (console)
    # dict[i] récupère la valeur associée à la clé i dans le dictionnaire
    print(dict[i])