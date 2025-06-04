resulting_first_line_indices = []

def count_characters_in_verse(target_character_count, verse_lines, start_line_index):

    accumulated_character_count = 0

    current_line_index = start_line_index

    while accumulated_character_count < target_character_count:

        accumulated_character_count += len(verse_lines[current_line_index])

        current_line_index += 1

    return [accumulated_character_count, current_line_index]


while True:

    number_of_verses = int(input())

    if number_of_verses == 0:
        break

    verse_lines = []

    for verse_line_index in range(number_of_verses):
        verse_lines.append(input())

    current_first_line_index = 0
    first_five_count = 0
    first_seven_count = 0
    second_five_count = 0
    second_seven_count = 0
    third_seven_count = 0

    candidate_start_index = -1

    search_index = 0

    while True:

        search_pointer = search_index

        first_five_count, search_pointer = count_characters_in_verse(5, verse_lines, search_pointer)
        if first_five_count == 5:

            first_seven_count, search_pointer = count_characters_in_verse(7, verse_lines, search_pointer)
            if first_seven_count == 7:

                second_five_count, search_pointer = count_characters_in_verse(5, verse_lines, search_pointer)
                if second_five_count == 5:

                    second_seven_count, search_pointer = count_characters_in_verse(7, verse_lines, search_pointer)
                    if second_seven_count == 7:

                        third_seven_count, search_pointer = count_characters_in_verse(7, verse_lines, search_pointer)
                        if third_seven_count == 7:

                            candidate_start_index = search_index
                            break

                        if candidate_start_index != -1:
                            break

                    if candidate_start_index != -1:
                        break

                if candidate_start_index != -1:
                    break

            if candidate_start_index != -1:
                break

        if candidate_start_index != -1:
            break

        search_index += 1

    resulting_first_line_indices.append(candidate_start_index + 1)

for index in resulting_first_line_indices:
    print(index)