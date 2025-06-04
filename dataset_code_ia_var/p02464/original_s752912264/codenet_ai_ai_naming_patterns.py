def read_integer():
    return int(input())

def read_integer_set():
    return set(map(int, input().split()))

def print_set_elements(sorted_set):
    for element in sorted_set:
        print(element)

def main():
    input_count_a = read_integer()
    set_a = read_integer_set()
    input_count_b = read_integer()
    set_b = read_integer_set()
    intersection_ab = set_a & set_b
    if intersection_ab:
        sorted_intersection = sorted(intersection_ab)
        print_set_elements(sorted_intersection)

if __name__ == "__main__":
    main()