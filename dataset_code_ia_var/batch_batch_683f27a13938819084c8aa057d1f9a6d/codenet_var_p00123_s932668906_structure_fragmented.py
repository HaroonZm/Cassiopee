import bisect

def get_input():
    return input()

def parse_input(inp):
    return list(map(float, inp.split()))

def get_m500_table():
    return [35.5, 37.5, 40, 43, 50, 55, 70]

def get_m1000_table():
    return [71, 77, 83, 89, 105, 116, 148]

def adjust_input_value(value):
    return value + 0.001

def get_rank_names():
    return ["AAA", "AA", "A", "B", "C", "D", "E", "NA"]

def calculate_index(table, value):
    return bisect.bisect_left(table, value)

def select_final_index(idx1, idx2):
    return max(idx1, idx2)

def get_rank(rank_table, idx):
    return rank_table[idx]

def process_one_case():
    inp = get_input()
    n, m = parse_input(inp)
    m500 = get_m500_table()
    m1000 = get_m1000_table()
    n_adj = adjust_input_value(n)
    m_adj = adjust_input_value(m)
    idx1 = calculate_index(m500, n_adj)
    idx2 = calculate_index(m1000, m_adj)
    final_idx = select_final_index(idx1, idx2)
    rank_table = get_rank_names()
    rank = get_rank(rank_table, final_idx)
    print(rank)

def main_loop():
    while True:
        try:
            process_one_case()
        except:
            break

main_loop()