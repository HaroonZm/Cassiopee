#!/usr/bin/env python3

def generate_points_sequence(n, m):
    """
    Génère une séquence de points pour n entités où les entités ayant un index
    supérieur à n//2 reçoivent chacune m points, et les autres reçoivent 0 point.

    Args:
        n (int): Le nombre total d'entités.
        m (int): Le nombre de points attribués à certaines entités.

    Returns:
        list of str: Une liste de chaînes représentant les points attribués à chaque entité.
    """
    # Initialiser la liste de points avec "0" pour chaque entité
    points = ["0"] * n

    # Attribuer 'm' points (convertis en chaîne) aux entités avec un index strictement supérieur à n//2
    # Cela correspond aux indices allant de n//2 + 1 à n-1 (indices de Python)
    for i in range(n // 2 + 1, n):
        points[i] = str(m)
    
    return points

def main():
    """
    Fonction principale qui lit l'entrée utilisateur, génère la séquence de points et l'affiche.
    """
    # Lire deux entiers depuis l'entrée standard (séparés par un espace)
    n, m = map(int, input().split())
    
    # Générer la séquence de points en fonction des valeurs fournies
    points = generate_points_sequence(n, m)
    
    # Afficher la séquence de points sous forme d'une chaîne d'entiers séparés par des espaces
    print(" ".join(points))

if __name__ == "__main__":
    main()