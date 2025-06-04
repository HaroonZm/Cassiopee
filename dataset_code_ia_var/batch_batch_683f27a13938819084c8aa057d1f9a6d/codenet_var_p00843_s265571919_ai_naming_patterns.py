def solve():
    from itertools import product as iter_product
    from sys import stdin as sys_stdin

    input_stream = sys_stdin

    while True:
        player_count, matrix_size = map(int, input_stream.readline().split())
        if player_count == 0:
            break

        card_patterns_list = []
        for player_idx in range(player_count):
            pattern_sets = []
            current_card_numbers = list(map(int, input_stream.readline().split()))
            diag_main, diag_anti = [], []
            for line_idx in range(matrix_size):
                pattern_sets.append(current_card_numbers[line_idx::matrix_size])  # vertical
                pattern_sets.append(current_card_numbers[line_idx * matrix_size: line_idx * matrix_size + matrix_size])  # horizontal
                diag_main.append(current_card_numbers[line_idx * matrix_size + line_idx])
                diag_anti.append(current_card_numbers[(matrix_size - 1) * (line_idx + 1)])
            pattern_sets.extend([diag_main, diag_anti])
            card_patterns_list.append(set(frozenset(pattern) for pattern in pattern_sets))

        if player_count == 2:
            min_result = min(len(pattern_1 | pattern_2)
                             for pattern_1, pattern_2 in iter_product(*card_patterns_list))
        elif player_count == 3:
            best_result = player_count * matrix_size + 1
            patterns_0, patterns_1, patterns_2 = card_patterns_list
            for pat_0 in patterns_0:
                if pat_0 in patterns_2:
                    for pat_1 in patterns_1:
                        if pat_1 & pat_0:
                            break
                    else:
                        continue

                for pat_1 in patterns_1:
                    union_01 = pat_0 | pat_1
                    subset_patterns_2 = set(p for p in patterns_2 if p <= union_01)
                    if subset_patterns_2:
                        if not pat_1 & set().union(*subset_patterns_2):
                            continue
                    for pat_2 in patterns_2:
                        merged_length = len(pat_2 | union_01)
                        if merged_length < best_result:
                            best_result = merged_length
            if best_result == player_count * matrix_size + 1:
                best_result = 0
            min_result = best_result
        else:
            best_result = player_count * matrix_size + 1
            patterns_0, patterns_1, patterns_2, patterns_3 = card_patterns_list
            for pat_0 in patterns_0:
                if pat_0 in patterns_2:
                    for pat_1 in patterns_1:
                        if pat_1 & pat_0:
                            break
                    else:
                        continue

                if pat_0 in patterns_3:
                    for pat_1, pat_2 in iter_product(patterns_1, patterns_2):
                        if pat_0 & pat_1 & pat_2:
                            break
                    else:
                        continue
                for pat_1 in patterns_1:
                    union_01 = pat_0 | pat_1
                    third_patterns = set(p2 for p2 in patterns_2 if p2 <= union_01)
                    if third_patterns:
                        if not pat_1 & set().union(*third_patterns):
                            continue

                    last_patterns = set(p3 for p3 in patterns_3 if p3 <= union_01)
                    if last_patterns:
                        if not pat_1 & set().union(*last_patterns):
                            continue

                    if third_patterns and last_patterns:
                        if not pat_1 & set().union(*third_patterns, *last_patterns):
                            continue

                    if not third_patterns and last_patterns:
                        for pat_2, pat_3 in iter_product(patterns_2, last_patterns):
                            if pat_1 & pat_2 & pat_3:
                                break
                        else:
                            continue
                    for pat_2 in patterns_2:
                        union_012 = pat_0 | pat_1 | pat_2
                        cur_last_patterns = set(p for p in patterns_3 if p <= union_012)
                        if cur_last_patterns:
                            intersec = pat_2 & set().union(*cur_last_patterns)
                            if not intersec:
                                continue

                            cur_first_patterns = set(p for p in patterns_0 if p <= union_012)
                            if cur_first_patterns <= cur_last_patterns:
                                cur_sec_patterns = set(p for p in patterns_1 if p <= union_012)
                                if not intersec & set().union(*cur_sec_patterns):
                                    continue
                        for pat_3 in patterns_3:
                            merged_length = len(union_012 | pat_3)
                            if merged_length < best_result:
                                best_result = merged_length
            if best_result == player_count * matrix_size + 1:
                best_result = 0
            min_result = best_result

        print(min_result)

solve()