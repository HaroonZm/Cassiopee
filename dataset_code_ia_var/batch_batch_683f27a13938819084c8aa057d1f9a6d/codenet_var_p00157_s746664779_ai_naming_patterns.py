while True:
    input_set_count = int(input())
    if input_set_count == 0:
        break
    doll_collection = []
    for input_doll_index in range(input_set_count):
        doll_height, doll_radius = [int(input_value) for input_value in input().split()]
        doll_collection.append((doll_height, doll_radius))
    input_extra_count = int(input())
    for input_extra_index in range(input_extra_count):
        extra_height, extra_radius = [int(input_value) for input_value in input().split()]
        doll_collection.append((extra_height, extra_radius))
    doll_collection_sorted = sorted(doll_collection, key=lambda doll_item: (doll_item[0], -doll_item[1]))
    radius_sequence = [doll_item[1] for doll_item in doll_collection_sorted]
    lis_lengths = [1 for _ in range(len(radius_sequence))]
    for current_index in range(len(radius_sequence)):
        for previous_index in range(current_index):
            if radius_sequence[previous_index] < radius_sequence[current_index]:
                lis_lengths[current_index] = max(lis_lengths[current_index], lis_lengths[previous_index] + 1)
    print(max(lis_lengths))