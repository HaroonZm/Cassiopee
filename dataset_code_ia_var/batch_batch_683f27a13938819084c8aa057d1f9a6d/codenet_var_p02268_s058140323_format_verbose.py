_
set_of_words_first_input = set(input().split())

_
set_of_words_second_input = set(input().split())

_
set_of_words_third_input = set(input().split())

set_of_words_fourth_input = set(input().split())

common_words_between_second_and_fourth_inputs = set_of_words_second_input & set_of_words_fourth_input

number_of_common_words = len(common_words_between_second_and_fourth_inputs)

print(number_of_common_words)