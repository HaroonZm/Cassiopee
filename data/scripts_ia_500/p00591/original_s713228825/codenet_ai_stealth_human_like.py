import sys

def find_min_index(row):
    # retourne l'indice de la plus petite valeur dans la ligne
    if len(row) == 0:
        return 0  # peut-être pas le meilleur choix si la ligne est vide...
    min_idx = 0
    for i in range(1, len(row)):
        if row[i] < row[min_idx]:
            min_idx = i
    return min_idx

def check_if_max_in_column(col_idx, row_idx, matrix):
    # regarde si l'élément matrix[row_idx][col_idx] est le max de sa colonne
    val = matrix[row_idx][col_idx]
    # parcours au-dessus du point
    for i in range(row_idx):
        if matrix[i][col_idx] > val:
            return False
    # parcours en-dessous y compris la ligne actuelle
    for i in range(row_idx + 1, len(matrix)):
        if matrix[i][col_idx] > val:
            return False
    return True

def find_saddle_point(matrix):
    for i, row in enumerate(matrix):
        min_pos = find_min_index(row)
        if check_if_max_in_column(min_pos, i, matrix):
            print(row[min_pos])
            return
    print(0)

lines = [line.strip() for line in sys.stdin]

index = 0
while index < len(lines):
    # si la ligne ne contient que 1 caractère (ex: '3\n'), on pense que c'est la taille
    if len(lines[index]) == 1 and lines[index].isdigit():
        n = int(lines[index])
        matrix = []
        for j in range(index+1, index+1+n):
            # split sur espaces et conversion en int
            row = [int(x) for x in lines[j].split()]
            matrix.append(row)
        find_saddle_point(matrix)
        index += n + 1
    else:
        # ligne "inattendue" on skip
        index += 1