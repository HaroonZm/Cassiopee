# Programme Python pour le classement d'équipes selon leurs points dans une ligue de football
# selon les règles données (victoire=3 points, défaite=0, nul=1)

def main():
    dataset_number = 0  # compteur de datasets pour gérer les sauts de ligne entre outputs

    while True:
        n = input().strip()
        if not n.isdigit():
            continue  # au cas où une ligne vide ou non valide apparaît
        n = int(n)
        if n == 0:
            break  # fin des données

        teams = []
        for i in range(n):
            line = input().strip()
            # Chaque ligne contient : nom w l d
            # nom jusqu'à 20 lettres, w,l,d entiers 0-9
            parts = line.split()
            name = parts[0]
            w = int(parts[1])
            l = int(parts[2])
            d = int(parts[3])
            points = 3 * w + 1 * d + 0 * l
            # on garde aussi l'indice d'entrée pour trier stable si égalité points
            teams.append((name, points, i))

        # Tri par points décroissants, si égalité, ordre d'entrée (i) croissant
        teams.sort(key=lambda x: (-x[1], x[2]))

        if dataset_number > 0:
            print()  # ligne vide entre datasets
        dataset_number += 1

        for team in teams:
            print(f"{team[0]},{team[1]}")

if __name__ == "__main__":
    main()