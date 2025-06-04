index_counter = 0
while True:
    if index_counter == 7:
        break
    value_first, value_second = map(int, input().split())
    result_difference = value_first - value_second
    print(result_difference)
    index_counter += 1