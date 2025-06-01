import sys

def find_universe_color(stars):
    """
    Cette fonction détermine si une couleur apparaît plus de la moitié du temps dans la liste stars.
    Si oui, renvoie cette couleur, sinon renvoie None.
    
    Approach:
    - Utilise la méthode du "majority element" (élément majoritaire) qui peut être trouvée en O(n) temps et O(1) espace.
    - Cette méthode maintient un candidat et un compteur.
    - Lorsqu'une nouvelle valeur est rencontrée:
      - Si le compteur est 0, on choisit cette valeur en candidat.
      - Sinon on incrémente ou décrémente le compteur selon que la valeur correspond au candidat.
    - A la fin, on vérifie si le candidat est effectivement majoritaire.
    """

    candidate = None
    count = 0

    # Première passe pour trouver un candidat potentiel
    for star in stars:
        if count == 0:
            candidate = star
            count = 1
        elif star == candidate:
            count += 1
        else:
            count -= 1

    # Seconde passe pour vérifier si le candidat est majoritaire
    if candidate is not None:
        actual_count = sum(1 for star in stars if star == candidate)
        if actual_count > len(stars) // 2:
            return candidate

    return None

def main():
    """
    Fonction principale qui lit les entrées, traite chaque test, et affiche le résultat.
    """
    input = sys.stdin.readline
    while True:
        n_line = input().strip()
        if n_line == '0':  # Fin des tests
            break

        n = int(n_line)
        stars = list(map(int, input().strip().split()))
        # On s'assure que la longueur correspond bien à n
        if len(stars) != n:
            # Si jamais l'entrée n'est pas conforme, on ignore ce test
            continue

        color = find_universe_color(stars)
        if color is not None:
            print(color)
        else:
            print("NO COLOR")

if __name__ == "__main__":
    main()