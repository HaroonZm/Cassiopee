def main():
    # Importation du module 'math' pour accéder aux fonctions mathématiques telles que sin, cos et radians
    import math

    # Création d'une liste appelée LIST avec trois éléments :
    # Le premier élément est 0 et représente la coordonnée X (initialisée à 0)
    # Le deuxième élément est 0 et représente la coordonnée Y (initialisée à 0)
    # Le troisième élément est math.radians(90), convertissant 90 degrés en radians (qui vaut pi/2),
    # et représente l'angle ou direction initiale en radians
    LIST = [0, 0, math.radians(90)]

    # Début d'une boucle infinie 'while True' qui ne s'arrêtera que par une instruction 'break'
    while True:
        # Affiche une invite pour l'utilisateur (optionnel mais généralement utilisé)
        # L'entrée de l'utilisateur doit être deux valeurs séparées par une virgule, par exemple : 10,45
        # La méthode input() récupère une chaîne de caractères depuis la console.
        # split(",") découpe cette chaîne là où il y a une virgule, créant une liste de deux éléments.
        # map(float, ...) convertit chaque élément de cette liste en un nombre à virgule flottante (float).
        # a et b reçoivent les deux valeurs saisies : 'a' sera la première valeur saisie, 'b' la seconde.
        a, b = map(float, input().split(","))

        # On vérifie si les deux valeurs saisies sont nulles (a == 0 et b == 0)
        if a == 0 and b == 0:
            # Si c'est le cas, on quitte la boucle avec 'break'.
            break
        else:
            # Sinon, on continue le traitement :
            # On convertit la valeur de 'b', exprimée en degrés, en radians,
            # car les fonctions trigonométriques de la bibliothèque math requièrent des radians.
            b = math.radians(b)

            # Mise à jour de la coordonnée X (LIST[0]) en ajoutant le déplacement vertical :
            # On utilise 'a * math.sin(LIST[2])' pour obtenir la composante selon Y du déplacement,
            # où 'a' est la distance à parcourir, et 'LIST[2]' est l'angle courant en radians.
            LIST[0] += a * math.sin(LIST[2])

            # Mise à jour de la coordonnée Y (LIST[1]) en ajoutant le déplacement horizontal :
            # 'a * math.cos(LIST[2])' donne la composante selon X du déplacement.
            LIST[1] += a * math.cos(LIST[2])

            # Mise à jour de la direction (LIST[2]) en modifiant l'angle courant :
            # On soustrait 'b' à l'angle courant, ce qui effectue une rotation négative d''b' radians.
            LIST[2] -= b

    # Une fois la boucle terminée (lorsque a et b valent tous deux 0), 
    # affichage de la valeur entière de la coordonnée Y (LIST[1])
    print(int(LIST[1]))

    # Affichage de la valeur entière de la coordonnée X (LIST[0])
    print(int(LIST[0]))

# Ce bloc vérifie si ce fichier est exécuté directement (et non importé comme module)
if __name__ == '__main__':
    # Appel de la fonction principale 'main()'
    main()