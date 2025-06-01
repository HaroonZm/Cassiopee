def update_counts_with_char(char):
    global counts_by_pattern
    new_counts_by_pattern = [0] * 7
    for current_pattern_index in range(7):
        if char in patterns[current_pattern_index]:
            for other_pattern_index in range(7):
                if patterns[current_pattern_index] & patterns[other_pattern_index]:
                    new_counts_by_pattern[current_pattern_index] += counts_by_pattern[other_pattern_index]
    counts_by_pattern = new_counts_by_pattern

number_of_characters = int(input())
input_string = input()
patterns = [
    set(["J"]),
    set(["O"]),
    set(["I"]),
    set(["J", "O"]),
    set(["J", "I"]),
    set(["O", "I"]),
    set(["J", "O", "I"])
]
counts_by_pattern = [1, 0, 0, 0, 0, 0, 0, 0]
for index in range(number_of_characters):
    update_counts_with_char(input_string[index])

print(sum(counts_by_pattern) % 10007)