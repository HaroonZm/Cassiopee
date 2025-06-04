while True:
    input_depth, input_width, input_height = map(int, input().split())
    if input_depth == 0:
        break
    min_diagonal_squared = min(
        input_depth ** 2 + input_width ** 2,
        input_width ** 2 + input_height ** 2,
        input_height ** 2 + input_depth ** 2
    )
    num_objects = int(input())
    for object_index in range(num_objects):
        object_diameter_squared = (int(input()) * 2) ** 2
        if object_diameter_squared > min_diagonal_squared:
            print("OK")
        else:
            print("NA")