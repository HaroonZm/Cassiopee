def create_empty_matrices():
    return [[[0 for _ in range(8)] for _ in range(8)] for _ in range(4)]

def get_titles():
    return ["0", "90", "180", "270"]

def input_row():
    return list(input())

def fill_original_matrix(a):
    for r in range(8):
        a[0][r] = input_row()

def rotate_once(prev, new):
    for r in range(8):
        for c in range(8):
            set_rotated_cell(new, c, 7 - r, get_cell(prev, r, c))

def get_cell(matrix, r, c):
    return matrix[r][c]

def set_rotated_cell(matrix, r, c, value):
    matrix[r][c] = value

def print_title(title):
    print(title)

def print_matrix(matrix):
    for r in range(8):
        print(''.join(matrix[r]))

def process_rotations(a, titles):
    for k in range(1, 4):
        print_title(titles[k])
        rotate_once(a[k-1], a[k])
        print_matrix(a[k])

def main():
    a = create_empty_matrices()
    titles = get_titles()
    fill_original_matrix(a)
    process_rotations(a, titles)

main()