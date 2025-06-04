def parse_input():
    return input()

def split_input(user_input):
    return user_input.split()

def map_to_int(str_list):
    return list(map(int, str_list))

def unpack_values(values):
    return values[0], values[1], values[2], values[3]

def compute_sub_total(a, b):
    return a + b

def compute_overlap(b_c_total, c):
    return b_c_total - c

def compute_final(n, a, b, c):
    sub_total = compute_sub_total(a, b)
    overlap = c
    return n - (sub_total - overlap)

def main():
    user_input = parse_input()
    str_list = split_input(user_input)
    values = map_to_int(str_list)
    n, a, b, c = unpack_values(values)
    result = compute_final(n, a, b, c)
    print(result)

main()