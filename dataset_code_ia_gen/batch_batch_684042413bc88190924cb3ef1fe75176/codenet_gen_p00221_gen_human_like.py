def is_correct(expected_num, said):
    if expected_num % 15 == 0:
        return said == "FizzBuzz"
    elif expected_num % 3 == 0:
        return said == "Fizz"
    elif expected_num % 5 == 0:
        return said == "Buzz"
    else:
        try:
            return int(said) == expected_num
        except ValueError:
            return False

import sys

for line in sys.stdin:
    if not line.strip():
        continue
    m_n = line.strip().split()
    if len(m_n) < 2:
        continue
    m, n = map(int, m_n)
    if m == 0 and n == 0:
        break
    s_list = []
    count = 0
    while count < n:
        s = sys.stdin.readline()
        if not s:
            break
        s_list.append(s.strip())
        count += 1

    players = list(range(1, m + 1))
    eliminated = set()
    current_number = 1
    turn_index = 0 # index in players list
    i = 0 # number of spoken turns so far

    while i < n:
        if len(players) - len(eliminated) <= 1:
            # Only one or zero players remain; stop processing
            break
        # find next player alive
        while players[turn_index] in eliminated:
            turn_index = (turn_index + 1) % m
        current_player = players[turn_index]
        said = s_list[i]
        if not is_correct(current_number, said):
            # eliminate current player
            eliminated.add(current_player)
            # next turn starts from next number after current_number
            current_number += 1
            # also move turn_index to next player alive for the next turn
            turn_index = (turn_index + 1) % m
            i += 1
            continue
        # if correct:
        current_number += 1
        turn_index = (turn_index + 1) % m
        i += 1

    survivors = [p for p in players if p not in eliminated]
    print(*sorted(survivors))