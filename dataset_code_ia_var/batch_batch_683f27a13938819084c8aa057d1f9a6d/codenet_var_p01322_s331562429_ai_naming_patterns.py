while True:
    pattern_count, query_count = map(int, input().split())
    if pattern_count == 0 and query_count == 0:
        break

    pattern_list = [[] for pattern_index in range(pattern_count)]

    for pattern_index in range(pattern_count):
        pattern_data = list(input().split())
        pattern_list[pattern_index] = [list(pattern_data[0]), int(pattern_data[1])]

    total_score = 0
    for query_index in range(query_count):
        query_chars = list(input())
        for pattern_index in range(pattern_count):
            match_found = True
            for char_index in range(8):
                if pattern_list[pattern_index][0][char_index] != '*' and pattern_list[pattern_index][0][char_index] != query_chars[char_index]:
                    match_found = False
                    break
            if match_found:
                total_score += pattern_list[pattern_index][1]
                break

    print(total_score)