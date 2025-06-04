def read_int_set_from_input():
    input()
    return set(map(int, input().split()))

def get_sorted_intersection(set_a, set_b):
    return sorted(set_a & set_b)

def print_elements_of_iterable(iterable):
    for element in iterable:
        print(element)

if __name__ == "__main__":
    set_a = read_int_set_from_input()
    set_b = read_int_set_from_input()
    intersection_sorted = get_sorted_intersection(set_a, set_b)
    print_elements_of_iterable(intersection_sorted)