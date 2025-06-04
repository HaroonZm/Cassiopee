import sys

def count_age_groups(ages):
    """
    Cette fonction reçoit une liste d'âges et compte le nombre de personnes dans chaque tranche d'âge définie :
    - 0~9
    - 10~19
    - 20~29
    - 30~39
    - 40~49
    - 50~59
    - 60 et plus
    Elle renvoie une liste de compte correspondant à chaque tranche dans cet ordre.
    """
    counts = [0]*7  # Initialisation des compteurs pour chaque tranche

    for age in ages:
        if age < 10:
            counts[0] += 1
        elif age < 20:
            counts[1] += 1
        elif age < 30:
            counts[2] += 1
        elif age < 40:
            counts[3] += 1
        elif age < 50:
            counts[4] += 1
        elif age < 60:
            counts[5] += 1
        else:
            counts[6] += 1
    return counts

def main():
    """
    Traitement des entrées multiples jusqu'à rencontrer une ligne unique "0".
    Pour chaque ensemble, on lit n puis n âges, on compte les personnes par tranche et on affiche les résultats.
    """
    input = sys.stdin.readline
    while True:
        line = input()
        if not line:
            break
        n = int(line)
        if n == 0:
            break

        ages = []
        # Lecture des âges
        for _ in range(n):
            age_line = input()
            if not age_line:
                break
            ages.append(int(age_line))

        counts = count_age_groups(ages)
        for c in counts:
            print(c)

if __name__ == "__main__":
    main()