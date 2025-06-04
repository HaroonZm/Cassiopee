import math

def main():
    """
    Lit les longueurs de deux côtés adjacents (a, b) et l'angle compris (C) en degrés d'un triangle à partir de l'entrée standard.
    Calcule ensuite l'aire, le périmètre et la hauteur relative consacrées à ce triangle.
    Affiche les résultats formatés à cinq décimales.
    """
    # Lecture des entrées utilisateur : a et b sont les longueurs des côtés, C est l'angle entre eux (en degrés)
    a, b, C = map(int, input().split())

    # Conversion de l'angle C de degrés en radians, requis pour les fonctions trigonométriques
    rC = math.radians(C)

    # Calcul des carrés des longueurs des côtés pour utilisation dans la formule du cosinus
    a2 = a ** 2
    b2 = b ** 2

    # Produit des deux côtés, utilisé dans plusieurs formules
    ab = a * b

    # Calcul de la longueur du troisième côté (c) via le théorème du cosinus :
    # c² = a² + b² - 2ab cos(C)
    c = math.sqrt(a2 + b2 - 2 * ab * math.cos(rC))

    # Calcul de l'aire (S) du triangle en utilisant la formule S = ab sin(C)/2
    S = ab * math.sin(rC) / 2

    # Calcul du périmètre (L) du triangle : somme des trois côtés
    L = a + b + c

    # Calcul de la hauteur (h) relative à la base 'a' : h = b sin(C)
    # (représente la hauteur du sommet opposé à a, projetée sur le côté a)
    h = b * math.sin(rC)

    # Affichage de l'aire, du périmètre et de la hauteur, chacun arrondi à cinq décimales
    print(f"{S:.5f} {L:.5f} {h:.5f}")

# Point d'entrée du programme
if __name__ == "__main__":
    main()