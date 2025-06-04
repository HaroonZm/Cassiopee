def read_input():
    return input()

def parse_first_line(line):
    return list(map(int, line.split()))

def parse_second_line(line):
    return list(map(int, line.split()))

def get_N_M_X(inputs):
    return inputs[0], inputs[1], inputs[2]

def import_bisect_module():
    import bisect
    return bisect

def find_insertion_index(bisect_module, array, value):
    return bisect_module.bisect_right(array, value)

def get_prefix(array, index):
    return array[:index]

def get_suffix(array, index):
    return array[index:]

def compute_length(lst):
    return len(lst)

def compute_min(a, b):
    return min(a, b)

def main():
    first_line = read_input()
    NMX = parse_first_line(first_line)
    N, M, X = get_N_M_X(NMX)
    second_line = read_input()
    A = parse_second_line(second_line)
    bisect_module = import_bisect_module()
    idx = find_insertion_index(bisect_module, A, X)
    prefix = get_prefix(A, idx)
    suffix = get_suffix(A, idx)
    len_prefix = compute_length(prefix)
    len_suffix = compute_length(suffix)
    result = compute_min(len_prefix, len_suffix)
    print(result)

main()