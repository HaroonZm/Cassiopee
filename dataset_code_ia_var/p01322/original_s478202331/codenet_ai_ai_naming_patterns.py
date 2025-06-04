def compare_patterns(pattern_a, pattern_b):
    chars_a = list(pattern_a)
    chars_b = list(pattern_b)
    chars_a.reverse()
    chars_b.reverse()
    while '*' in chars_a:
        chars_a.remove('*')
    is_match = True
    for idx in range(len(chars_a)):
        if chars_a[idx] != chars_b[idx]:
            is_match = False
            break
    return is_match

while True:
    num_patterns, num_strings = map(int, input().split())
    if num_patterns == 0 and num_strings == 0:
        break

    pattern_list = []
    value_list = []
    for pattern_idx in range(num_patterns):
        pattern_str, value_str = input().split()
        pattern_list.append(pattern_str)
        value_list.append(int(value_str))

    total_cost = 0
    for string_idx in range(num_strings):
        input_string = input()
        for pattern_idx in range(num_patterns):
            if compare_patterns(pattern_list[pattern_idx], input_string):
                total_cost += value_list[pattern_idx]
    print(total_cost)