while True:

    try:
        input_number_of_items, input_group_size = map(int, raw_input().split())
        
        if input_number_of_items == 0:
            break

        item_values_list = sorted(map(int, raw_input().split()), reverse=True)

        for index in range(input_group_size - 1, input_number_of_items, input_group_size):
            item_values_list[index] = 0

        total_value = sum(item_values_list)
        print total_value

    except:
        pass