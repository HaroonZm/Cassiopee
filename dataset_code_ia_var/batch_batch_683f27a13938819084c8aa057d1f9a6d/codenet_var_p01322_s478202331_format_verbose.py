def compare_reversed_patterns_without_asterisk(pattern_string, target_string):
    
    reversed_pattern_characters = list(pattern_string)
    reversed_target_characters = list(target_string)

    reversed_pattern_characters.reverse()
    reversed_target_characters.reverse()
    
    while '*' in reversed_pattern_characters:
        reversed_pattern_characters.remove('*')
    
    are_patterns_equal = True

    for character_index in range(len(reversed_pattern_characters)):
        if reversed_pattern_characters[character_index] != reversed_target_characters[character_index]:
            are_patterns_equal = False
            break

    return are_patterns_equal

while True:
    number_of_patterns, number_of_inputs = map(int, input().split())

    if number_of_patterns == 0 and number_of_inputs == 0:
        break

    pattern_list = []
    pattern_monetary_values = []

    for pattern_index in range(number_of_patterns):
        pattern_string, pattern_value_string = input().split()
        pattern_list.append(pattern_string)
        pattern_monetary_values.append(int(pattern_value_string))

    total_cost = 0

    for input_index in range(number_of_inputs):
        input_string = input()
        for pattern_index in range(number_of_patterns):
            if compare_reversed_patterns_without_asterisk(pattern_list[pattern_index], input_string) == True:
                total_cost += pattern_monetary_values[pattern_index]

    print(total_cost)