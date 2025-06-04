def find_pair_with_modulo_pattern():
    element_count = int(input())
    element_list = [int(element_value) for element_value in input().split()]
    for first_index in range(element_count):
        for second_index in range(first_index + 1, element_count):
            if abs(element_list[first_index] - element_list[second_index]) % (element_count - 1) == 0:
                print(f"{element_list[first_index]} {element_list[second_index]}")
                return

find_pair_with_modulo_pattern()