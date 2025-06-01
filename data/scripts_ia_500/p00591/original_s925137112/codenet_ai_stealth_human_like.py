import sys

while True:
    line = sys.stdin.readline().strip()
    if not line:
        break  # au cas où la ligne est vide
    n = int(line)
    if n == 0:
        break
    students_scores = []
    for _ in range(n):
        scores = list(map(int, sys.stdin.readline().strip().split()))
        students_scores.append(scores)

    # Trouve les minimums par ligne (étudiant)
    min_flags = []
    for row in students_scores:
        row_min = min(row)
        min_flags.append([score == row_min for score in row])

    # Trouve les maximums par colonne (exercice)
    max_flags = []
    for col in zip(*students_scores):
        col_max = max(col)
        max_flags.append([score == col_max for score in col])

    # Transposer max_flags pour avoir la même forme que min_flags
    max_flags_t = list(zip(*max_flags))

    candidates = [0]  # Liste des scores candidats, 0 au cas où aucun
    for i, (min_row, max_row) in enumerate(zip(min_flags, max_flags_t)):
        for j, (is_min, is_max) in enumerate(zip(min_row, max_row)):
            if is_min and is_max:
                candidates.append(students_scores[i][j])

    print(max(candidates))  # Affiche le max trouvé ou 0 par défaut