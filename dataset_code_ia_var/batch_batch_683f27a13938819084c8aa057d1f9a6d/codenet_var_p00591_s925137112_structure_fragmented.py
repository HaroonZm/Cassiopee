import sys

def read_input():
    return sys.stdin.readline().rstrip()

def parse_int(s):
    return int(s)

def read_n():
    line = read_input()
    return parse_int(line)

def read_student_line():
    line = read_input()
    return list(map(parse_int, line.split(' ')))

def read_students(n):
    students = []
    for _ in range(n):
        students.append(read_student_line())
    return students

def get_min_of_row(row):
    return min(row)

def get_max_of_col(col):
    return max(col)

def flag_min_in_row(row):
    min_v = get_min_of_row(row)
    return [s == min_v for s in row]

def flag_max_in_col(col):
    max_v = get_max_of_col(col)
    return [s == max_v for s in col]

def compute_s_list(students):
    return [flag_min_in_row(row) for row in students]

def compute_t_list(students):
    columns = list(zip(*students))
    return [flag_max_in_col(col) for col in columns]

def transpose(matrix):
    return list(zip(*matrix))

def process_positions(s_list, t_list, students):
    result = [0]
    transposed_t_list = transpose(t_list)
    for i, (s_row, t_row) in enumerate(zip(s_list, transposed_t_list)):
        combined = zip(s_row, t_row)
        for j, d in enumerate(combined):
            if all(d):
                result.append(students[i][j])
    return result

def handle_case(n):
    students = read_students(n)
    s_list = compute_s_list(students)
    t_list = compute_t_list(students)
    pos_values = process_positions(s_list, t_list, students)
    return max(pos_values)

def main_loop():
    while True:
        n = read_n()
        if n == 0:
            break
        result = handle_case(n)
        print(result)

def main():
    main_loop()

main()