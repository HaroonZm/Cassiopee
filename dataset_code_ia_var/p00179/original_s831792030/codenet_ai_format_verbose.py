primary_colors_set = set(["r", "g", "b"])

while True:
    input_worm_string = raw_input()
    if input_worm_string == "0":
        break

    worm_length = len(input_worm_string)
    worms_queue = [input_worm_string]
    checked_worms_set = set(input_worm_string)
    current_level_count = 1
    current_depth = 0
    has_uniform_worm = False

    while True:
        for _ in range(current_level_count):
            current_worm = worms_queue.pop(0)
            if current_worm in checked_worms_set:
                continue
            else:
                checked_worms_set.add(current_worm)
            if len(set(current_worm)) == 1:
                has_uniform_worm = True
                break
            for char_index in range(worm_length - 1):
                if current_worm[char_index] != current_worm[char_index + 1]:
                    candidate_worm = current_worm[:]
                    next_color = list(primary_colors_set - set(candidate_worm[char_index:char_index + 2]))[0]
                    candidate_worm = candidate_worm[:char_index] + 2 * next_color + candidate_worm[char_index + 2:]
                    if candidate_worm not in worms_queue:
                        worms_queue.append(candidate_worm)
        current_level_count = len(worms_queue)
        if has_uniform_worm or current_level_count == 0:
            break
        current_depth += 1
        if current_depth > 15:
            break
    print current_depth if has_uniform_worm else "NA"