number_of_test_cases = int(raw_input())

for test_case_index in xrange(number_of_test_cases):

    input_height, input_width = map(int, raw_input().split())

    grid_characters = [list(raw_input()) for row_index in xrange(input_height)]

    minimal_column_by_object = {}
    maximal_column_by_object = {}
    minimal_row_by_object = {}
    maximal_row_by_object = {}

    present_objects = set()

    for row_index in xrange(input_height):
        for column_index in xrange(input_width):
            current_character = grid_characters[row_index][column_index]
            if current_character == '.':
                continue
            minimal_column_by_object[current_character] = min(minimal_column_by_object.get(current_character, 99), column_index)
            maximal_column_by_object[current_character] = max(maximal_column_by_object.get(current_character, -1), column_index)
            minimal_row_by_object[current_character] = min(minimal_row_by_object.get(current_character, 99), row_index)
            maximal_row_by_object[current_character] = max(maximal_row_by_object.get(current_character, -1), row_index)
            present_objects.add(current_character)

    if not present_objects:
        print "SAFE"
        continue

    is_rectangle_well_formed = True

    adjacency_graph_by_object = { object_label: set() for object_label in present_objects }
    in_degree_by_object = { object_label: 0 for object_label in present_objects }

    for analyzed_object in present_objects:
        for row in xrange(minimal_row_by_object[analyzed_object], maximal_row_by_object[analyzed_object]+1):
            for column in xrange(minimal_column_by_object[analyzed_object], maximal_column_by_object[analyzed_object]+1):
                character_in_cell = grid_characters[row][column]
                if character_in_cell == '.':
                    is_rectangle_well_formed = False
                    break
                if character_in_cell != analyzed_object:
                    adjacency_graph_by_object[analyzed_object].add(character_in_cell)
            if not is_rectangle_well_formed:
                break
        if not is_rectangle_well_formed:
            break

    if not is_rectangle_well_formed:
        print "SUSPICIOUS"
        continue

    for source_object in present_objects:
        for adjacent_object in adjacency_graph_by_object[source_object]:
            in_degree_by_object[adjacent_object] += 1

    remaining_objects_count = len(present_objects)
    processed_objects = set()

    for iteration_object in present_objects:
        for candidate_object in present_objects:
            if in_degree_by_object[candidate_object] == 0 and candidate_object not in processed_objects:
                for adjacent_object in adjacency_graph_by_object[candidate_object]:
                    in_degree_by_object[adjacent_object] -= 1
                processed_objects.add(candidate_object)
                remaining_objects_count -= 1

    if remaining_objects_count:
        print "SUSPICIOUS"
    else:
        print "SAFE"