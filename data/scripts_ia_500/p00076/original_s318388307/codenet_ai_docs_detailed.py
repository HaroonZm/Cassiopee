def main():
    """
    Exécute une boucle infinie qui lit des entiers 'n' depuis l'entrée standard.
    Pour chaque entier 'n' différent de -1 (condition d'arrêt), calcule un nombre
    complexe 'p' selon une suite particulière, puis affiche la partie réelle et
    imaginaire de ce nombre avec deux décimales.
    """
    while True:
        # Lire un entier depuis l'entrée utilisateur
        n = int(input())
        # Condition d'arrêt : si n + 1 == 0, c'est-à-dire si n == -1, sortir de la boucle
        if n == -1:
            break

        # Initialisation du point complexe p à 1 + 0j sur le plan complexe
        p = 1 + 0j

        # Itérer n - 1 fois pour calculer la position finale de p
        for _ in range(n - 1):
            # Calculer un vecteur orthogonal à p en multipliant p par l'unité imaginaire 1j
            d = p * 1j
            # Normaliser le vecteur d pour qu'il ait une norme (longueur) égale à 1
            d /= abs(d)
            # Mettre à jour p en ajoutant ce vecteur unitaire orthogonal normalisé
            p += d

        # Afficher la partie réelle et imaginaire de p, formatées avec deux décimales
        print("{:.2f}\n{:.2f}".format(p.real, p.imag))


if __name__ == "__main__":
    main()