number_of_rows, number_of_columns = map(int, input().split())

first_table_characters = ''
second_table_characters = ''

for current_row_index in range(2 * number_of_rows):

    current_row_characters = input()

    if current_row_index < number_of_rows:
        first_table_characters += current_row_characters
    else:
        second_table_characters += current_row_characters

number_of_differences = 0

for character_in_first_table, character_in_second_table in zip(first_table_characters, second_table_characters):

    if character_in_first_table != character_in_second_table:
        number_of_differences += 1

print(number_of_differences)