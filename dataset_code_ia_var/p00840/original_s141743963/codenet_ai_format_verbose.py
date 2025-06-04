def compute_max_bridge_length_with_readable_variables():
    from itertools import combinations
    from sys import stdin

    input_stream = stdin

    def enumerate_bridge_positions(current_base_position, stone_weights_list):
        stone_weights_key = tuple(stone_weights_list)

        if stone_weights_key in memoized_combinations:
            return set(
                (current_base_position + left_span, current_base_position + right_span)
                for left_span, right_span in memoized_combinations[stone_weights_key]
            )

        possible_end_edges = set()
        possible_bridge_positions = set()

        for num_selected_stones in range(1, len(stone_weights_list)):
            for selected_stones_tuple in combinations(stone_weights_list, num_selected_stones):
                group1_stones = list(selected_stones_tuple)
                group2_stones = stone_weights_list[:]
                for single_stone in group1_stones:
                    group2_stones.remove(single_stone)

                total_weight_group1 = sum(group1_stones)
                total_weight_group2 = sum(group2_stones)
                total_weight = total_weight_group1 + total_weight_group2

                new_base_group1 = current_base_position - total_weight_group2 / total_weight
                new_base_group2 = current_base_position + total_weight_group1 / total_weight

                left_bridge_ends = enumerate_bridge_positions(new_base_group1, group1_stones)
                right_bridge_ends = enumerate_bridge_positions(new_base_group2, group2_stones)

                for left_edge_start, left_edge_end in left_bridge_ends:
                    for right_edge_start, right_edge_end in right_bridge_ends:
                        minimum_left_edge = min(left_edge_start, right_edge_start)
                        maximum_right_edge = max(left_edge_end, right_edge_end)
                        possible_end_edges.add(
                            (minimum_left_edge - current_base_position, maximum_right_edge - current_base_position)
                        )
                        possible_bridge_positions.add((minimum_left_edge, maximum_right_edge))

        memoized_combinations[stone_weights_key] = possible_end_edges
        return possible_bridge_positions

    number_of_test_cases = int(input_stream.readline())

    memoized_combinations = dict()

    for test_case_index in range(number_of_test_cases):

        maximum_bridge_allowed_length = float(input_stream.readline())
        number_of_stones = int(input_stream.readline())

        individual_stone_weights = sorted(
            int(input_stream.readline()) for _ in range(number_of_stones)
        )

        for stone_weight in individual_stone_weights:
            memoized_combinations[(stone_weight,)] = {(0, 0)}

        all_possible_bridge_spans = enumerate_bridge_positions(
            0,
            individual_stone_weights
        )

        try:
            maximal_span_within_limit = max(
                right_end - left_end
                for left_end, right_end in all_possible_bridge_spans
                if (right_end - left_end) < maximum_bridge_allowed_length
            )
            print(maximal_span_within_limit)
        except ValueError:
            print(-1)

compute_max_bridge_length_with_readable_variables()