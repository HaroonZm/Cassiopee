def solve(input_stream, number_of_lines, number_of_exchanges):

    forward_forward_exchanges = []
    forward_reverse_exchanges = []
    reverse_forward_exchanges = []
    
    for exchange_index in range(number_of_exchanges):
        exchange_line = input_stream.readline().rstrip()
        line_index_1, direction_1, _, line_index_2, direction_2 = exchange_line
        
        line_index_1 = int(line_index_1)
        line_index_2 = int(line_index_2)
        
        if direction_1 == 'E':
            if direction_2 == 'W':
                forward_forward_exchanges.append((line_index_1, line_index_2))
            else:
                forward_reverse_exchanges.append((line_index_1, line_index_2))
        else:
            if direction_2 == 'E':
                forward_forward_exchanges.append((line_index_2, line_index_1))
            else:
                reverse_forward_exchanges.append((line_index_2, line_index_1))
    
    initial_forward_state = []
    for line_index in range(number_of_lines):
        forward_train_string = input_stream.readline().rstrip()
        if forward_train_string == '-':
            initial_forward_state.append('')
        else:
            initial_forward_state.append(forward_train_string)
    forward_states_visited = {'|'.join(initial_forward_state): 0}
    forward_search_frontier = [initial_forward_state]
    
    initial_backward_state = []
    for line_index in range(number_of_lines):
        backward_train_string = input_stream.readline().rstrip()
        if backward_train_string == '-':
            initial_backward_state.append('')
        else:
            initial_backward_state.append(backward_train_string)
    backward_states_visited = {'|'.join(initial_backward_state): 0}
    backward_search_frontier = [initial_backward_state]
    
    for step_number in range(1, 4):
        
        next_forward_frontier = []
        for current_forward_state in forward_search_frontier:
            
            for index_from, index_to in forward_forward_exchanges:
                copied_trains = current_forward_state[:]
                combined_train = current_forward_state[index_from] + current_forward_state[index_to]
                for split_point in range(len(combined_train) + 1):
                    copied_trains[index_from] = combined_train[:split_point]
                    copied_trains[index_to] = combined_train[split_point:]
                    state_key = '|'.join(copied_trains)
                    if state_key not in forward_states_visited:
                        if state_key in backward_states_visited:
                            return backward_states_visited[state_key] + step_number
                        forward_states_visited[state_key] = step_number
                        next_forward_frontier.append(copied_trains[:])
            
            for index_from, index_to in forward_reverse_exchanges:
                copied_trains = current_forward_state[:]
                combined_train = current_forward_state[index_from] + current_forward_state[index_to][::-1]
                for split_point in range(len(combined_train) + 1):
                    copied_trains[index_from] = combined_train[:split_point]
                    copied_trains[index_to] = combined_train[split_point:][::-1]
                    state_key = '|'.join(copied_trains)
                    if state_key not in forward_states_visited:
                        if state_key in backward_states_visited:
                            return backward_states_visited[state_key] + step_number
                        forward_states_visited[state_key] = step_number
                        next_forward_frontier.append(copied_trains[:])
            
            for index_from, index_to in reverse_forward_exchanges:
                copied_trains = current_forward_state[:]
                combined_train = current_forward_state[index_from][::-1] + current_forward_state[index_to]
                for split_point in range(len(combined_train) + 1):
                    copied_trains[index_from] = combined_train[:split_point][::-1]
                    copied_trains[index_to] = combined_train[split_point:]
                    state_key = '|'.join(copied_trains)
                    if state_key not in forward_states_visited:
                        if state_key in backward_states_visited:
                            return backward_states_visited[state_key] + step_number
                        forward_states_visited[state_key] = step_number
                        next_forward_frontier.append(copied_trains[:])
        
        forward_search_frontier = next_forward_frontier
        
        if step_number == 3:
            return 6
        
        next_backward_frontier = []
        for current_backward_state in backward_search_frontier:
            
            for index_from, index_to in forward_forward_exchanges:
                copied_trains = current_backward_state[:]
                combined_train = current_backward_state[index_from] + current_backward_state[index_to]
                for split_point in range(len(combined_train) + 1):
                    copied_trains[index_from] = combined_train[:split_point]
                    copied_trains[index_to] = combined_train[split_point:]
                    state_key = '|'.join(copied_trains)
                    if state_key not in backward_states_visited:
                        if state_key in forward_states_visited:
                            return forward_states_visited[state_key] + step_number
                        backward_states_visited[state_key] = step_number
                        next_backward_frontier.append(copied_trains[:])
            
            for index_from, index_to in forward_reverse_exchanges:
                copied_trains = current_backward_state[:]
                combined_train = current_backward_state[index_from] + current_backward_state[index_to][::-1]
                for split_point in range(len(combined_train) + 1):
                    copied_trains[index_from] = combined_train[:split_point]
                    copied_trains[index_to] = combined_train[split_point:][::-1]
                    state_key = '|'.join(copied_trains)
                    if state_key not in backward_states_visited:
                        if state_key in forward_states_visited:
                            return forward_states_visited[state_key] + step_number
                        backward_states_visited[state_key] = step_number
                        next_backward_frontier.append(copied_trains[:])
            
            for index_from, index_to in reverse_forward_exchanges:
                copied_trains = current_backward_state[:]
                combined_train = current_backward_state[index_from][::-1] + current_backward_state[index_to]
                for split_point in range(len(combined_train) + 1):
                    copied_trains[index_from] = combined_train[:split_point][::-1]
                    copied_trains[index_to] = combined_train[split_point:]
                    state_key = '|'.join(copied_trains)
                    if state_key not in backward_states_visited:
                        if state_key in forward_states_visited:
                            return forward_states_visited[state_key] + step_number
                        backward_states_visited[state_key] = step_number
                        next_backward_frontier.append(copied_trains[:])
        
        backward_search_frontier = next_backward_frontier

def main():
    from sys import stdin
    input_stream = stdin
    
    while True:
        input_line = input_stream.readline()
        number_of_lines, number_of_exchanges = map(int, input_line.split())
        
        if number_of_lines == 0:
            break
        
        print(solve(input_stream, number_of_lines, number_of_exchanges))

main()