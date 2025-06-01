def check_puzzle_solved(number_list):
    unique_numbers = set(number_list)
    for number in unique_numbers:
        if number_list.count(number) >= 2:
            working_list = number_list[:]
            working_list.remove(number)
            working_list.remove(number)
            for check_number in unique_numbers:
                count = working_list.count(check_number)
                if count == 4:
                    if check_number + 1 in working_list and check_number + 2 in working_list:
                        for _ in range(4):
                            working_list.remove(check_number)
                        working_list.remove(check_number + 1)
                        working_list.remove(check_number + 2)
                elif count == 3:
                    for _ in range(3):
                        working_list.remove(check_number)
                elif working_list.count(check_number + 1) >= count and working_list.count(check_number + 2) >= count:
                    for _ in range(count):
                        working_list.remove(check_number)
                        working_list.remove(check_number + 1)
                        working_list.remove(check_number + 2)
            if not working_list:
                return True
    return False

while True:
    try:
        input_numbers = list(map(int, list(input())))
        valid_results = []
        for candidate_number in range(1, 10):
            if input_numbers.count(candidate_number) <= 3 and check_puzzle_solved(input_numbers + [candidate_number]):
                valid_results.append(candidate_number)
        if valid_results:
            print(*valid_results)
        else:
            print(0)
    except EOFError:
        break