def judge_number_divisibility(number):
    if number % 15 == 0:
        return "FizzBuzz"
    if number % 5 == 0:
        return "Buzz"
    if number % 3 == 0:
        return "Fizz"
    return str(number)

while True:
    max_value, iterations = map(int, raw_input().split())
    if max_value == 0 and iterations == 0:
        break

    candidate_numbers = range(1, max_value + 1)
    current_index = 0

    for turn in range(1, iterations + 1):
        user_input = raw_input()
        if len(candidate_numbers) > 1:
            expected_string = judge_number_divisibility(turn)
            if expected_string != user_input:
                del candidate_numbers[current_index]
                current_index %= len(candidate_numbers)
            else:
                current_index = (current_index + 1) % len(candidate_numbers)

    print(" ".join(map(str, candidate_numbers)))