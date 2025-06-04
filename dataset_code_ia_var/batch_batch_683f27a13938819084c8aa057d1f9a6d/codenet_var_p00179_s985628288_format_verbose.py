possible_colors = set(["r", "g", "b"])

while True:
    input_worm = raw_input()
    
    if input_worm == "0":
        break

    worm_length = len(input_worm)
    queue_length = 1
    step_count = 0
    found_uniform_color = False

    current_worm_set = set([input_worm])

    while True:
        current_worm_list = list(current_worm_set)
        current_worm_set = set()

        for _ in range(queue_length):
            current_worm = current_worm_list.pop(0)

            if len(set(current_worm)) == 1:
                found_uniform_color = True
                break

            for char_index in range(worm_length - 1):
                if current_worm[char_index] != current_worm[char_index + 1]:
                    missing_color = list(possible_colors - set(current_worm[char_index:char_index+2]))[0]
                    new_worm = current_worm[:char_index] + 2 * missing_color + current_worm[char_index + 2:]
                    current_worm_set.add(new_worm)

        queue_length = len(current_worm_set)

        if found_uniform_color:
            break

        step_count += 1

        if step_count > 15:
            break

    print step_count if found_uniform_color else "NA"