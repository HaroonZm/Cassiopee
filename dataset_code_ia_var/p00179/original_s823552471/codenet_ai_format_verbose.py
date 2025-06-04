import Queue

color_pair_to_new_colors = {
    'rg': 'bb',
    'gr': 'bb',
    'gb': 'rr',
    'bg': 'rr',
    'br': 'gg',
    'rb': 'gg',
}

while True:
    input_string = raw_input()
    
    if input_string == '0':
        break
    
    transition_queue = Queue.PriorityQueue()
    
    input_length = len(input_string)
    
    transformation_costs = {input_string: 0}
    
    transition_queue.put((0, input_string))
    
    uniform_color_targets = [
        'r' * input_length,
        'g' * input_length,
        'b' * input_length
    ]
    
    minimum_operations = -1
    
    while not transition_queue.empty():
        current_cost, current_sequence = transition_queue.get()
        
        if current_sequence in uniform_color_targets:
            minimum_operations = current_cost
            break
        
        if transformation_costs[current_sequence] < current_cost:
            continue
        
        for pair_index in xrange(input_length - 1):
            color_pair = current_sequence[pair_index:pair_index + 2]
            
            if color_pair[0] != color_pair[1]:
                new_sequence = (
                    current_sequence[:pair_index] +
                    color_pair_to_new_colors[color_pair] +
                    current_sequence[pair_index + 2:]
                )
                
                if (new_sequence not in transformation_costs or
                    current_cost + 1 < transformation_costs[new_sequence]):
                    transformation_costs[new_sequence] = current_cost + 1
                    transition_queue.put((current_cost + 1, new_sequence))
    
    print "NA" if minimum_operations < 0 else minimum_operations