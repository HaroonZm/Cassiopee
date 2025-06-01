def read_dimensions():
    return map(int, input().split())

def read_matrix(h):
    matrix = []
    for _ in range(h):
        row = read_row()
        matrix.append(row)
    return matrix

def read_row():
    return list(map(int, input().split()))

def initialize_answer():
    return 1010101010

def calculate_min_distance(i, j, h, w, matrix):
    total = 0
    for k in range(h):
        for l in range(w):
            total += compute_contribution(i, j, k, l, matrix)
    return total

def compute_contribution(i, j, k, l, matrix):
    distance = min(abs(i - k), abs(j - l))
    return distance * matrix[k][l]

def find_min_answer(h, w, matrix, current_min):
    for i in range(h):
        for j in range(w):
            now = calculate_min_distance(i, j, h, w, matrix)
            current_min = update_min_answer(current_min, now)
    return current_min

def update_min_answer(current_min, candidate):
    if candidate < current_min:
        return candidate
    return current_min

def main():
    h, w = read_dimensions()
    matrix = read_matrix(h)
    ans = initialize_answer()
    ans = find_min_answer(h, w, matrix, ans)
    print_answer(ans)

def print_answer(ans):
    print(ans)

main()