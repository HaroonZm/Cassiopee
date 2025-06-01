def create_paper(size):
    return [[0] * size for _ in range(size)]

def read_input():
    try:
        line = input()
        return list(map(int, line.split(',')))
    except:
        return None

def in_manhattan_distance(i, j, x, y, dist):
    return abs(x - i) + abs(y - j) <= dist

def in_chebyshev_distance(i, j, x, y, dist):
    return abs(x - i) <= dist and abs(y - j) <= dist

def update_cell(paper, i, j):
    paper[i][j] += 1

def apply_effect_type_1(paper, x, y):
    for i in range(10):
        for j in range(10):
            if in_manhattan_distance(i, j, x, y, 1):
                update_cell(paper, i, j)

def apply_effect_type_2(paper, x, y):
    for i in range(10):
        for j in range(10):
            if in_chebyshev_distance(i, j, x, y, 1):
                update_cell(paper, i, j)

def apply_effect_other(paper, x, y):
    for i in range(10):
        for j in range(10):
            if in_manhattan_distance(i, j, x, y, 2):
                update_cell(paper, i, j)

def process_input_line(paper, x, y, s):
    if s == 1:
        apply_effect_type_1(paper, x, y)
    elif s == 2:
        apply_effect_type_2(paper, x, y)
    else:
        apply_effect_other(paper, x, y)

def flatten_list(lst):
    return sum(lst, [])

def count_zeros(lst):
    return lst.count(0)

def max_value(lst):
    return max(lst)

def main():
    paper = create_paper(10)
    while True:
        values = read_input()
        if values is None:
            break
        x, y, s = values
        process_input_line(paper, x, y, s)
    ls = flatten_list(paper)
    print(count_zeros(ls))
    print(max_value(ls))

main()