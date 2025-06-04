from numpy import array

def read_input():
    return open(0).read().split()

def split_input(input_data):
    return list(map(int, input_data))

def extract_parameters(params):
    n = params[0]
    a = params[1]
    b = params[2]
    p = params[3:]
    return n, a, b, p

def create_array(p):
    return array(p)

def get_counts(c, a, b):
    return sum(c <= a), sum((a < c) & (c <= b)), sum(b < c)

def get_min_value(counts):
    return min(counts)

def main():
    input_data = read_input()
    params = split_input(input_data)
    n, a, b, p = extract_parameters(params)
    c = create_array(p)
    counts = get_counts(c, a, b)
    minimum = get_min_value(counts)
    print(minimum)

main()