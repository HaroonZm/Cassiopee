MODULO = 1000000007

text = input()
pattern = input()

length_text = len(text)
length_pattern = len(pattern)

dp_table = [[0] * (length_pattern + 1) for _ in range(length_text + 1)]

for index_in_text in range(length_text + 1):
    
    dp_table[index_in_text][0] = 1

for current_position_in_text in range(1, length_text + 1):
    
    for current_position_in_pattern in range(1, length_pattern + 1):
        
        matched_char = (text[current_position_in_text - 1] == pattern[current_position_in_pattern - 1])
        
        dp_table[current_position_in_text][current_position_in_pattern] = (
            dp_table[current_position_in_text - 1][current_position_in_pattern]
            + dp_table[current_position_in_text - 1][current_position_in_pattern - 1] * matched_char
        ) % MODULO

print(dp_table[length_text][length_pattern])