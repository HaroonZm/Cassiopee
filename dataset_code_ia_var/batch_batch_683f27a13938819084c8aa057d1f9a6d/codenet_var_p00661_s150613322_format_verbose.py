while True:

    number_of_times, sequence_length = map(int, input().split())

    if number_of_times == 0:
        break

    time_values_list = list(map(int, input().split()))

    if 1 in time_values_list:
        number_of_times = 0

    print(number_of_times / 2)