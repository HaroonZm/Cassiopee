import sys
from collections import defaultdict

def check_material_safety(material_id):

    if material_check_status[material_id] > 0:
        return material_check_status[material_id]

    material_check_status[material_id] = 1  # Mark as checking

    top_edge, bottom_edge, left_edge, right_edge = material_rectangle[material_id]

    for row_index in range(top_edge, bottom_edge + 1):
        for col_index in range(left_edge, right_edge + 1):

            if material_grid[row_index][col_index] == ".":

                material_check_status[material_id] = 3  # Suspicious due to hole inside rectangle
                return 3

            elif material_grid[row_index][col_index] != material_id:

                conflicting_material_id = material_grid[row_index][col_index]

                if material_check_status[conflicting_material_id] == 1:
                    material_check_status[material_id] = 3  # Suspicious due to cyclic dependency
                    return 3

                conflict_check_result = check_material_safety(conflicting_material_id)

                if conflict_check_result == 3:
                    material_check_status[material_id] = 3  # Suspicious since dependent is suspicious
                    return 3

    material_check_status[material_id] = 2  # Mark as safe
    return 2

number_of_test_cases = int(sys.stdin.readline())

for test_case_index in range(number_of_test_cases):

    grid_height, grid_width = map(int, sys.stdin.readline().split())

    material_grid = [sys.stdin.readline().rstrip('\n') for _ in range(grid_height)]
    material_rectangle = defaultdict(list)  # Each material id: [top_edge, bottom_edge, left_edge, right_edge]

    # Find top edge for each material
    for row_index in range(grid_height):
        for col_index in range(grid_width):
            material_id = material_grid[row_index][col_index]
            if material_id != "." and len(material_rectangle[material_id]) < 1:
                material_rectangle[material_id].append(row_index)

    # Find bottom edge for each material
    for row_index in reversed(range(grid_height)):
        for col_index in range(grid_width):
            material_id = material_grid[row_index][col_index]
            if material_id != "." and len(material_rectangle[material_id]) < 2:
                material_rectangle[material_id].append(row_index)

    # Find left edge for each material
    for col_index in range(grid_width):
        for row_index in range(grid_height):
            material_id = material_grid[row_index][col_index]
            if material_id != "." and len(material_rectangle[material_id]) < 3:
                material_rectangle[material_id].append(col_index)

    # Find right edge for each material
    for col_index in reversed(range(grid_width)):
        for row_index in range(grid_height):
            material_id = material_grid[row_index][col_index]
            if material_id != "." and len(material_rectangle[material_id]) < 4:
                material_rectangle[material_id].append(col_index)

    material_check_status = defaultdict(lambda: 0)  # 0: unvisited, 1: checking, 2: safe, 3: suspicious

    for material_id in material_rectangle.keys():
        if check_material_safety(material_id) == 3:
            print("SUSPICIOUS")
            break
    else:
        print("SAFE")