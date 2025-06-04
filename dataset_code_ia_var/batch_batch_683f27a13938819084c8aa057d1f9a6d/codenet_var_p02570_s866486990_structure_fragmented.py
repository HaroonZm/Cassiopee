def read_input():
    return input()

def parse_input(raw_input):
    return map(int, raw_input.split())

def unpack_values(parsed_input):
    D, T, S = parsed_input
    return D, T, S

def compute_threshold(T, S):
    return T * S

def is_possible(D, threshold):
    return D <= threshold

def output_result(possible):
    if possible:
        print("Yes")
    else:
        print("No")

def main():
    raw_input = read_input()
    parsed_input = parse_input(raw_input)
    D, T, S = unpack_values(parsed_input)
    threshold = compute_threshold(T, S)
    possible = is_possible(D, threshold)
    output_result(possible)

main()