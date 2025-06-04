number_of_test_cases = int(input())

for current_test_case_index in range(number_of_test_cases):

    grid_height, grid_width = map(int, input().split())

    character_grid = [list(input()) for _ in range(grid_height)]

    character_bounding_box_coordinates = {}  # key=character, value=(min_x, max_x, min_y, max_y)
    unresolved_characters = []

    for row_index in range(grid_height):
        for column_index in range(grid_width):
            current_character = character_grid[row_index][column_index]
            if current_character in character_bounding_box_coordinates:
                min_x, max_x, min_y, max_y = character_bounding_box_coordinates[current_character]
                character_bounding_box_coordinates[current_character] = (
                    min(column_index, min_x),
                    max(column_index, max_x),
                    min(row_index, min_y),
                    max(row_index, max_y),
                )
            else:
                character_bounding_box_coordinates[current_character] = (column_index, column_index, row_index, row_index)
                unresolved_characters.append(current_character)

    while unresolved_characters:

        unresolved_characters_snapshot = unresolved_characters[:]

        for character_to_process in unresolved_characters:

            invalid_rectangle_found = False
            min_x, max_x, min_y, max_y = character_bounding_box_coordinates[character_to_process]

            for current_x in range(min_x, max_x + 1):
                for current_y in range(min_y, max_y + 1):
                    inspected_character = character_grid[current_y][current_x]
                    if inspected_character not in (character_to_process, "#"):
                        invalid_rectangle_found = True
                        break
                if invalid_rectangle_found:
                    break

            else:
                for rectangle_row in range(min_y, max_y + 1):
                    character_grid[rectangle_row][min_x:max_x + 1] = ["#"] * (max_x - min_x + 1)
                unresolved_characters.remove(character_to_process)

        if unresolved_characters_snapshot == unresolved_characters:
            print("SUSPICIOUS")
            break

    else:
        print("SAFE")