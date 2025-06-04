MODULO_CONSTANT = 1000000007

input_text = input()
target_subsequence = input()

length_input_text = len(input_text)
length_target_subsequence = len(target_subsequence)

number_of_ways = [0] * (length_target_subsequence + 1)
number_of_ways[0] = 1

for index_input_text in range(1, length_input_text + 1):

    current_character = input_text[index_input_text - 1]

    for index_target in range(length_target_subsequence, 0, -1):

        if current_character == target_subsequence[index_target - 1]:

            number_of_ways[index_target] += number_of_ways[index_target - 1]
            number_of_ways[index_target] %= MODULO_CONSTANT

print(number_of_ways[length_target_subsequence])