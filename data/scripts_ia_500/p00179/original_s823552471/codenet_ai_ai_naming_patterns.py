import Queue

COLOR_TRANSFORMATIONS = {
    'rg': 'bb', 'gr': 'bb',
    'gb': 'rr', 'bg': 'rr',
    'br': 'gg', 'rb': 'gg',
}

while True:
    input_string = raw_input()
    if input_string == '0':
        break

    priority_queue = Queue.PriorityQueue()
    string_length = len(input_string)
    cost_dict = {input_string: 0}
    priority_queue.put((0, input_string))
    target_strings = ['r' * string_length, 'g' * string_length, 'b' * string_length]
    answer = -1

    while not priority_queue.empty():
        current_cost, current_string = priority_queue.get()
        if current_string in target_strings:
            answer = current_cost
            break
        if cost_dict[current_string] < current_cost:
            continue
        for index in xrange(string_length - 1):
            pair = current_string[index:index + 2]
            if pair[0] != pair[1]:
                transformed_string = (
                    current_string[:index]
                    + COLOR_TRANSFORMATIONS[pair]
                    + current_string[index + 2:]
                )
                new_cost = current_cost + 1
                if transformed_string not in cost_dict or new_cost < cost_dict[transformed_string]:
                    cost_dict[transformed_string] = new_cost
                    priority_queue.put((new_cost, transformed_string))

    if answer < 0:
        print "NA"
    else:
        print answer