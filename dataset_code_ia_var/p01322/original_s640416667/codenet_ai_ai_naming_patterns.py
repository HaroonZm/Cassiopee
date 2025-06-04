while True:
    pattern_count, ticket_count = map(int, input().split())
    if pattern_count == 0:
        break
    pattern_list = [input().split() for _ in range(pattern_count)]
    ticket_list = [input() for _ in range(ticket_count)]
    total_score = 0
    for ticket_str in ticket_list:
        for pattern_entry in pattern_list:
            pattern_str, pattern_value = pattern_entry
            for char_index in range(len(ticket_str)):
                if pattern_str[char_index] != "*" and ticket_str[char_index] != pattern_str[char_index]:
                    break
            else:
                total_score += int(pattern_value)
                break
    print(total_score)