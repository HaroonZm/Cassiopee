while True:

    try:
        number_of_elements, group_size = map(int, input().split())
        
        elements_list = list(map(int, input().split()))
        
        elements_list.sort(reverse=True)
        
        for group_end_index in range(group_size - 1, number_of_elements, group_size):
            elements_list[group_end_index] = 0
        
        total_sum = sum(elements_list)
        
        print(total_sum)

    except:
        break