import math

def main():
    """
    Lit les longueurs des côtés a, b et la mesure de l'angle C en degrés,
    puis calcule et affiche (au format 8 décimales) dans l'ordre suivant :
      1. L'aire du triangle formé par a, b et C.
      2. Le périmètre du triangle (somme des trois côtés).
      3. La hauteur du triangle mesurée depuis le côté 'a' (hauteur abaissée depuis 'a').
    """
    # Lire les valeurs d'entrée utilisateur en tant que float : longueur des côtés a, b, angle C (en degrés)
    a, b, C = map(float, input().split())
    
    # Convertir l'angle C de degrés en radians pour les fonctions trigonométriques
    C_rad = math.pi * C / 180

    # Calculer l'aire du triangle en utilisant la formule: (1/2)*a*b*sin(C)
    area = 0.5 * a * b * math.sin(C_rad)
    print("{0:.8f}".format(area))

    # Calculer la longueur du troisième côté par le théorème du cosinus
    c = math.sqrt(a**2 + b**2 - 2 * a * b * math.cos(C_rad))
    # Calculer le périmètre en sommant les trois côtés
    perimeter = a + b + c
    print("{0:.8f}".format(perimeter))

    # Calculer la hauteur abaissée depuis le côté 'a' (hauteur relative à 'a')
    # h = b * sin(C)
    height = b * math.sin(C_rad)
    print("{0:.8f}".format(height))

if __name__ == "__main__":
    main()