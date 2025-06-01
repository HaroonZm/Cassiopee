while True:
    
    number_of_customers = int(input())
    
    if number_of_customers == 0:
        break
    
    individual_waiting_times = []
    accumulated_waiting_times = []
    
    for customer_index in range(number_of_customers):
        waiting_time = int(input())
        individual_waiting_times.append(waiting_time)
    
    individual_waiting_times.sort()
    
    for current_index, current_wait_time in enumerate(individual_waiting_times):
        total_wait_before_current = sum(individual_waiting_times[:current_index])
        accumulated_waiting_times.append(total_wait_before_current)
    
    total_accumulated_waiting_time = sum(accumulated_waiting_times)
    print(total_accumulated_waiting_time)