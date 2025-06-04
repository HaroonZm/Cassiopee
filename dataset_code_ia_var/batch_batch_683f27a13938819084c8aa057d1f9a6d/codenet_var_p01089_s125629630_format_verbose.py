while True:

    user_input = input()

    if user_input == 0:
        break

    sequence_input = raw_input()

    unique_state_set = set()
    current_lock_state = 0
    state_transition_list = []

    for character in sequence_input:

        if character == 'u':
            current_lock_state = 0

        else:
            button_bitmask = (current_lock_state, 1 << int(character))
            if button_bitmask not in unique_state_set:
                state_transition_list.append(button_bitmask)
                unique_state_set.add(button_bitmask)
            current_lock_state |= 1 << int(character)

    current_index = 0
    is_safe = 1

    while current_index < len(state_transition_list) and is_safe:

        lock_state_1, trigger_1 = state_transition_list[current_index]

        if lock_state_1 & trigger_1 == trigger_1:
            is_safe = 0

        for previous_index in xrange(current_index):

            lock_state_2, trigger_2 = state_transition_list[previous_index]

            if lock_state_1 & lock_state_2 == 0 and trigger_1 & lock_state_2 == trigger_1:
                if trigger_2 & lock_state_1 == trigger_2:
                    is_safe = 0

                combined_state = (lock_state_1 | lock_state_2, trigger_2)
                if combined_state not in unique_state_set:
                    state_transition_list.append(combined_state)
                    unique_state_set.add(combined_state)

        current_index += 1

    print "SAFE" * is_safe or "UNSAFE"