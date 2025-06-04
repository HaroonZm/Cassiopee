def is_strictly_increasing_with_one_drop_allowed(sequence):

    largest_so_far = 0
    second_largest_so_far = 0

    for current_number in sequence:

        if current_number > largest_so_far:
            largest_so_far = current_number

        elif current_number > second_largest_so_far:
            second_largest_so_far = current_number

        else:
            return 0

    return 1

number_of_cases = int(raw_input())

for _ in range(number_of_cases):

    integer_sequence = map(int, raw_input().split())

    if is_strictly_increasing_with_one_drop_allowed(integer_sequence):
        print "YES"
    else:
        print "NO"