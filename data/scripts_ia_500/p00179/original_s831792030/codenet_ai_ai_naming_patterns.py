color_set = set(["r", "g", "b"])
while True:
    input_string = raw_input()
    if input_string == "0":
        break
    string_length = len(input_string)
    queue = [input_string]
    visited_set = set(input_string)
    level_length = 1
    iteration_count = 0
    found_flag = 0
    while True:
        for _ in range(level_length):
            current_string = queue.pop(0)
            if current_string in visited_set:
                continue
            else:
                visited_set.add(current_string)
            if len(set(current_string)) == 1:
                found_flag = 1
                break
            for index in range(string_length - 1):
                if current_string[index] != current_string[index + 1]:
                    temp_string = current_string[:]
                    next_color = list(color_set - set(current_string[index:index + 2]))[0]
                    temp_string = temp_string[:index] + 2 * next_color + temp_string[index + 2:]
                    if temp_string not in queue:
                        queue.append(temp_string)
        level_length = len(queue)
        if found_flag or level_length == 0:
            break
        iteration_count += 1
        if iteration_count > 15:
            break
    print iteration_count if found_flag else "NA"