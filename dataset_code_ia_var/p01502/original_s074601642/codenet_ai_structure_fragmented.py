def get_input():
    return raw_input()

def to_int(value):
    return int(value)

def split_input(line):
    return line.split(" ")

def map_to_ints(str_list):
    return list(map(int, str_list))

def read_matrix_row():
    line = get_input()
    splitted = split_input(line)
    mapped = map_to_ints(splitted)
    return mapped

def build_matrix(N):
    matrix = []
    for _ in range(N):
        row = read_matrix_row()
        matrix.append(row)
    return matrix

def min_cost_per_pair(cost, i, j):
    if cost[i][j] <= cost[j][i]:
        return cost[i][j]
    else:
        return cost[j][i]

def accumulate_cost_for_i(cost, i):
    total = 0
    for j in range(i):
        current = min_cost_per_pair(cost, i, j)
        total += current
    return total

def calculate_total_cost(cost, N):
    total_cost = 0
    for i in range(N):
        total_cost += accumulate_cost_for_i(cost, i)
    return total_cost

def print_output(value):
    print value

def main():
    N_raw = get_input()
    N = to_int(N_raw)
    cost = build_matrix(N)
    total_cost = calculate_total_cost(cost, N)
    print_output(total_cost)

main()