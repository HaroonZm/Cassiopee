import queue

def convert_str_list_to_int(str_list):
    joined_str = ''
    for char in str_list:
        joined_str += char
    return int(joined_str)

def main():
    input_target_count = int(input())
    if input_target_count < 10:
        print(input_target_count)
        return

    lunlun_queue = queue.Queue()
    for initial_digit in range(1, 10):
        lunlun_queue.put(initial_digit)

    current_count = 9

    next_digit_map = [
        [0, 1],
        [0, 1, 2],
        [1, 2, 3],
        [2, 3, 4],
        [3, 4, 5],
        [4, 5, 6],
        [5, 6, 7],
        [6, 7, 8],
        [7, 8, 9],
        [8, 9]
    ]

    while not lunlun_queue.empty():
        current_number_list = list(str(lunlun_queue.get()))
        last_digit = int(current_number_list[-1])
        for next_digit in next_digit_map[last_digit]:
            current_count += 1
            candidate_number_list = current_number_list + [str(next_digit)]
            if current_count == input_target_count:
                print(convert_str_list_to_int(candidate_number_list))
                return
            else:
                lunlun_queue.put(convert_str_list_to_int(candidate_number_list))

main()