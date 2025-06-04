import collections as collections_module

while True:
    number_of_inputs = int(input())
    if number_of_inputs == 0:
        break

    input_elements = raw_input().split()

    for current_length in range(1, number_of_inputs + 1):
        current_counter = collections_module.Counter(input_elements[:current_length])
        most_common_elements = current_counter.most_common() + [('', 0)]

        if (
            most_common_elements[0][1]
            > most_common_elements[1][1] + number_of_inputs - current_length
        ):
            print(most_common_elements[0][0], current_length)
            break
    else:
        print("TIE")