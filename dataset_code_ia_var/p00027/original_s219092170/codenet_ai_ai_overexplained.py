# Importation du module 'date' à partir de la bibliothèque standard 'datetime'
# Le module 'datetime' fournit des classes pour manipuler des dates et des heures
from datetime import date

# Importation du module 'calendar' de la bibliothèque standard
# Le module 'calendar' fournit des fonctions qui permettent de manipuler et d'afficher des calendriers
import calendar

# Début d'une boucle infinie avec while True
# La condition 'True' signifie que la boucle se répétera sans fin jusqu'à un break explicite
while True:
    # Demande à l'utilisateur de saisir des entrées via la fonction input()
    # La fonction input() récupère une ligne de texte entrée par l'utilisateur au clavier
    # Par convention, on attend que l'utilisateur saisisse deux nombres séparés par un espace (par exemple : "5 23")
    # La méthode split() sépare la chaîne en une liste de chaînes, en utilisant l'espace par défaut comme séparateur
    # map(int, ...) applique la fonction int (pour convertir en entier) à chaque élément de la liste obtenue avec split()
    # Les deux valeurs converties sont ensuite affectées respectivement aux variables 'm' (mois) et 'd' (jour)
    m, d = map(int, input().split())
    
    # Vérification de la condition d'arrêt de la boucle
    # 'if not m' : en Python, 0 est considéré comme False en contexte booléen,
    # donc cette condition teste si l'utilisateur a entré 0 pour 'm' (le mois)
    # Si le mois vaut 0, on rompt la boucle avec 'break'
    if not m:
        break

    # Si la condition précédente n'est pas satisfaite, on exécute la ligne suivante
    # On crée d'abord un objet date correspondant à l'année 2004, au mois 'm', et au jour 'd'
    # La classe 'date' nécessite trois entiers : année, mois, jour
    # La méthode 'weekday()' de l'objet date retourne un entier correspondant au jour de la semaine :
    # 0 = lundi, 1 = mardi, ..., 6 = dimanche
    # 'calendar.day_name' est une séquence contenant le nom des jours de la semaine en anglais dans l'ordre (Monday, Tuesday, ...)
    # On utilise l'indice retourné par .weekday() pour obtenir le nom du jour de la semaine
    # Ce nom est affiché grâce à la fonction print()
    print(calendar.day_name[date(2004, m, d).weekday()])