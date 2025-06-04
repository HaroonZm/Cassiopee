import math  # Importation du module math, qui fournit des fonctions mathématiques standards, comme cosinus et sinus.

def main():  # Définition de la fonction principale appelée main, qui contiendra toute la logique de notre programme.
    p = [0, 0]  # Création d'une liste p avec deux éléments, représentant les coordonnées x et y du point courant (position initiale à l'origine).
    x = math.radians(90)  # La variable x va stocker l'angle courant en radians. math.radians convertit 90 degrés en radians, ce qui correspond à l'axe vertical positif.
    while True:  # Début d'une boucle infinie; elle s'exécutera indéfiniment jusqu'à ce qu'une instruction break l'interrompe.
        # Lecture de l'entrée utilisateur demandant deux valeurs séparées par une virgule.
        # On utilise input() pour lire la ligne, split(",") pour séparer la chaîne au niveau de la virgule,
        # et map(int, ...) pour convertir chaque partie en entier.
        d, angle = map(int, input().split(","))
        # On analyse la condition d'arrêt : si les deux valeurs saisies sont 0, cela signifie que l'utilisateur veut terminer le programme.
        if d == 0 and angle == 0:  # Vérifie que les deux variables sont égales à 0.
            break  # Quitte la boucle while en cours grâce à break.
        # Mise à jour de la position horizontale (p[0], c'est-à-dire la coordonnée x).
        # On ajoute à la position existante la distance d multipliée par le cosinus de l'angle courant.
        # math.cos(x) donne le cosinus de l'angle x (en radians). Cela sert à projeter d dans la direction horizontale.
        p[0] += math.cos(x) * d
        # Mise à jour de la position verticale (p[1], c'est-à-dire la coordonnée y).
        # Pareil que précédemment, on projette la distance d dans la direction verticale à l'aide du sinus.
        p[1] += math.sin(x) * d
        # Mise à jour de la direction globale pour les prochains mouvements : on soustrait à l'angle courant 'x' la valeur de 'angle' (convertie en radians).
        # Cela correspond à une rotation de 'angle' degrés (vers la droite si angle positif).
        x -= math.radians(angle)
    # Sortie de la boucle : on prépare les résultats pour affichage.
    # On convertit les coordonnées flottantes vers des entiers en prenant la partie entière, ce qui supprime toute partie décimale.
    for i in (0, 1):  # Boucle sur les indices 0 et 1, pour couvrir les deux coordonnées de la liste.
        p[i] = int(p[i])  # Conversion en entier de chaque valeur de la liste.
    # Affichage du résultat : les deux coordonnées sont affichées l'une après l'autre, chacune sur une nouvelle ligne.
    # print prend les éléments de la liste p et les affiche, séparés par un retour à la ligne grâce à sep="\n".
    print(*p, sep="\n")

if __name__ == "__main__":  # Cette condition spéciale permet de vérifier si ce fichier Python est exécuté directement (et non importé dans un autre script).
    main()  # Si c'est le cas, on appelle la fonction main.