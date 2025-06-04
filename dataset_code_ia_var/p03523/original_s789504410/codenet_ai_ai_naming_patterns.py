input_string = input()
pattern_length = 4
clear_indices = [0, 4, 6, 8]
match_found = False

for main_index in range(pattern_length ** 2):
    char_list = ["A", "K", "I", "H", "A", "B", "A", "R", "A"]
    for pattern_index in range(pattern_length):
        if ((main_index >> pattern_index) & 1):
            char_list[clear_indices[pattern_index]] = ""
    candidate_string = "".join(char_list)
    if candidate_string == input_string:
        print("YES")
        match_found = True
        break

if not match_found:
    print("NO")