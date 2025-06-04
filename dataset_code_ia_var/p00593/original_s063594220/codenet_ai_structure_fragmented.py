def get_otehon():
    return [
        [1,2,6,7,15,16,28,29,45],
        [3,5,8,14,17,27,30,44],
        [4,9,13,18,26,31,43],
        [10,12,19,25,32,42],
        [11,20,24,33,41],
        [21,23,34,40],
        [22,35,39],
        [36,38],
        [37]
    ]

def get_input_number():
    return int(raw_input())

def make_zero_matrix(N):
    return [[0 for _ in range(N)] for _ in range(N)]

def fill_upper_triangle(N, hairetu, otehon):
    for i in range(N):
        for j in range(N):
            if i + j < N:
                hairetu[i][j] = otehon[i][j]

def compute_mirror_value(N, i, j, hairetu):
    return N*N + 1 - hairetu[N-1-i][N-1-j]

def fill_lower_triangle(N, hairetu):
    for i in range(N):
        for j in range(N):
            if i + j >= N:
                hairetu[i][j] = compute_mirror_value(N, i, j, hairetu)

def format_number(num):
    num = str(num)
    if len(num) == 1:
        return "  " + num
    return " " + num

def build_line(N, i, hairetu):
    strn = ""
    for j in range(N):
        strn += format_number(hairetu[i][j])
    return strn

def print_case_number(n):
    print "Case " + str(n) + ":"

def print_matrix(N, hairetu):
    for i in range(N):
        print build_line(N, i, hairetu)

def process_single_case(n, N, otehon):
    hairetu = make_zero_matrix(N)
    fill_upper_triangle(N, hairetu, otehon)
    fill_lower_triangle(N, hairetu)
    print_case_number(n)
    print_matrix(N, hairetu)

def main_loop():
    otehon = get_otehon()
    n = 0
    while True:
        N = get_input_number()
        if N == 0:
            break
        n += 1
        process_single_case(n, N, otehon)

main_loop()