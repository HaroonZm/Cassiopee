def read_integer():
    return int(input())

def input_split():
    return input().split()

def parse_input_line(inp):
    P = int(inp[1])
    A = int(inp[2])
    B = int(inp[3])
    C = int(inp[4])
    D = int(inp[5])
    E = int(inp[6])
    F = int(inp[7])
    S = int(inp[8])
    M = int(inp[9])
    return inp[0], P, A, B, C, D, E, F, S, M

def compute_time(A, B, C, M, D, E):
    return A + B + C + M * (D + E)

def compute_money(M, F, S, P):
    return M * F * S - P

def build_entry(name, money, time):
    return [name, money / time]

def collect_entries(N):
    data = []
    for _ in range(N):
        inp = input_split()
        name, P, A, B, C, D, E, F, S, M = parse_input_line(inp)
        time = compute_time(A, B, C, M, D, E)
        money = compute_money(M, F, S, P)
        entry = build_entry(name, money, time)
        data.append(entry)
    return data

def sort_entries_by_name(data):
    return sorted(data, key=lambda x: x[0])

def sort_entries_by_ratio(data):
    return sorted(data, key=lambda x: -x[1])

def output_entries(data):
    for entry in data:
        print(entry[0])

def output_hash():
    print('#')

def process_block(N):
    entries = collect_entries(N)
    entries = sort_entries_by_name(entries)
    entries = sort_entries_by_ratio(entries)
    output_entries(entries)
    output_hash()

def main_loop():
    while True:
        N = read_integer()
        if N == 0:
            break
        process_block(N)

main_loop()