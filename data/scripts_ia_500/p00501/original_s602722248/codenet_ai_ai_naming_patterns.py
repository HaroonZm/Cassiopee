def find_all_indices(character, string):
    indices_list, start_index = [], 0
    while True:
        found_index = string.find(character, start_index)
        if found_index == -1:
            break
        else:
            indices_list.append(found_index)
            start_index = found_index + 1
    return indices_list

def matches_pattern(pattern, text):
    if text.find(pattern) != -1:
        return True
    pattern_first_indices = find_all_indices(pattern[0], text)
    pattern_second_indices = find_all_indices(pattern[1], text)
    if len(pattern_first_indices) == 0 or len(pattern_second_indices) == 0:
        return False
    for first_idx in pattern_first_indices:
        for second_idx in pattern_second_indices:
            if first_idx >= second_idx:
                continue
            step = second_idx - first_idx
            match_found = True
            for offset in range(2, len(pattern)):
                check_index = first_idx + offset * step
                if check_index >= len(text) or pattern[offset] != text[check_index]:
                    match_found = False
                    break
            if match_found:
                return True
    return False

number_of_texts = int(input())
pattern_string = input().strip()
input_texts = [input().strip() for _ in range(number_of_texts)]
match_count = 0
for text in input_texts:
    if matches_pattern(pattern_string, text):
        match_count += 1
print(match_count)