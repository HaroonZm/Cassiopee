def process_sets_intersection():
    input_set1_length = raw_input()
    input_set1_elements = set(raw_input().strip().split(' '))
    input_set2_length = raw_input()
    input_set2_elements = set(raw_input().strip().split(' '))
    intersection_count = len(input_set1_elements & input_set2_elements)
    print intersection_count

if __name__ == '__main__':
    process_sets_intersection()