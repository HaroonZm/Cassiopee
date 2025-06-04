def fizzbuzz_evaluate(number):
    if number % 15 == 0:
        return "FizzBuzz"
    if number % 5 == 0:
        return "Buzz"
    if number % 3 == 0:
        return "Fizz"
    return str(number)

while True:
    input_row = raw_input()
    param_count, round_count = map(int, input_row.split())
    if param_count == 0 and round_count == 0:
        break
    candidate_list = range(1, param_count + 1)
    candidate_index = 0
    for round_number in range(1, round_count + 1):
        user_choice = raw_input()
        if len(candidate_list) > 1:
            if fizzbuzz_evaluate(round_number) != user_choice:
                del candidate_list[candidate_index]
                candidate_index %= len(candidate_list)
            else:
                candidate_index = (candidate_index + 1) % len(candidate_list)
    print " ".join(map(str, candidate_list))