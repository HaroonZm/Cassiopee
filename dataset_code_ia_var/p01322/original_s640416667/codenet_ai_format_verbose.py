while True:

    number_of_patterns, number_of_tickets = map(int, input().split())

    if number_of_patterns == 0:
        break

    lottery_patterns = [input().split() for _ in range(number_of_patterns)]

    lottery_tickets = [input() for _ in range(number_of_tickets)]

    total_winning_amount = 0

    for ticket in lottery_tickets:

        for pattern_details in lottery_patterns:

            pattern, reward = pattern_details

            for character_index in range(len(ticket)):

                if pattern[character_index] != '*' and ticket[character_index] != pattern[character_index]:
                    break

            else:
                total_winning_amount += int(reward)
                break

    print(total_winning_amount)