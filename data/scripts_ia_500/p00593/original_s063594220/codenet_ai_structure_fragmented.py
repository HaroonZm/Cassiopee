otehon = [[1,2,6,7,15,16,28,29,45],
          [3,5,8,14,17,27,30,44],
          [4,9,13,18,26,31,43],
          [10,12,19,25,32,42],
          [11,20,24,33,41],
          [21,23,34,40],
          [22,35,39],
          [36,38],
          [37]]

def convert_number_to_str(num):
    num_str = str(num)
    if len(num_str) == 1:
        return "  " + num_str
    return " " + num_str

def initialize_hairetu(N):
    return [[0 for _ in range(N)] for _ in range(N)]

def fill_upper_triangle(hairetu, N):
    for i in range(N):
        for j in range(N):
            if i + j < N:
                hairetu[i][j] = otehon[i][j]

def fill_lower_triangle(hairetu, N):
    for i in range(N):
        for j in range(N):
            if i + j >= N:
                hairetu[i][j] = N * N + 1 - hairetu[N - 1 - i][N - 1 - j]

def construct_line(hairetu, i, N):
    line_str = ""
    for j in range(N):
        line_str += convert_number_to_str(hairetu[i][j])
    return line_str

def print_case_number(case_num):
    print("Case " + str(case_num) + ":")

def read_integer():
    return int(raw_input())

def process_case(case_num):
    N = read_integer()
    if N == 0:
        return False
    hairetu = initialize_hairetu(N)
    fill_upper_triangle(hairetu, N)
    fill_lower_triangle(hairetu, N)
    print_case_number(case_num)
    for i in range(N):
        print(construct_line(hairetu, i, N))
    return True

def main():
    case_num = 0
    while True:
        case_num += 1
        if not process_case(case_num):
            break

main()