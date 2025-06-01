while True:
    
    number_of_people, step_count = map(int, raw_input().split())
    
    if number_of_people == 0 and step_count == 0:
        break
    
    people_status = [1 for index in range(number_of_people)]
    
    remaining_people = number_of_people
    current_count = 0
    counting_active = True
    
    while counting_active:
        for person_index in range(number_of_people):
            if people_status[person_index] == 1:
                current_count += 1
                
                if current_count == step_count:
                    people_status[person_index] = 0
                    current_count = 0
                    remaining_people -= 1
                    
                    if remaining_people == 1:
                        counting_active = False
                        break
                        
    last_person_standing = people_status.index(1) + 1
    print last_person_standing