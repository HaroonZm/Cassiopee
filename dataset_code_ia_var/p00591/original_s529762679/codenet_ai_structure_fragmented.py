def get_user_input():
    return input()

def check_break_condition(n):
    return n == 0

def get_raw_input():
    return raw_input()

def parse_row(row):
    return list(map(int, row.strip().split()))

def build_L(n):
    result = []
    for _ in range(n):
        row = get_raw_input()
        parsed = parse_row(row)
        result.append(parsed)
    return result

def get_min_of_row(row):
    return min(row)

def build_S(L):
    mins = []
    for row in L:
        mins.append(get_min_of_row(row))
    return set(mins)

def get_column(L, col_index):
    column = []
    for row in L:
        column.append(row[col_index])
    return column

def get_max_of_list(lst):
    return max(lst)

def check_max_in_S(maxInt, S):
    return maxInt in S

def print_value(val):
    print val

def process_columns(L, S, n):
    for j in range(n):
        t = get_column(L, j)
        maxInt = get_max_of_list(t)
        if check_max_in_S(maxInt, S):
            print_value(maxInt)
            return True
    return False

def main_loop():
    while True:
        n = get_user_input()
        if check_break_condition(n):
            break
        L = build_L(n)
        S = build_S(L)
        if not process_columns(L, S, n):
            print_value(0)

main_loop()