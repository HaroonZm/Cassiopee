input_count = int(input())
initial_letters = ["M", "A", "R", "C", "H"]
letter_counts = [0] * 5
total_combinations = 0

for input_index in range(input_count):
    input_word = input()
    word_initial = input_word[0]
    if word_initial in initial_letters:
        letter_index = initial_letters.index(word_initial)
        letter_counts[letter_index] += 1

for first_index in range(3):
    for second_index in range(first_index + 1, 4):
        for third_index in range(second_index + 1, 5):
            total_combinations += (letter_counts[first_index]
                                   * letter_counts[second_index]
                                   * letter_counts[third_index])
print(total_combinations)