number_of_entries = int(input())

event_sequence = list(map(int, input().split()))

present_animals_stack = []

for current_event_index in range(number_of_entries):
    
    current_animal_event = event_sequence[current_event_index]
    
    if current_animal_event > 0:
        
        if current_animal_event in present_animals_stack:
            print(current_event_index + 1)
            break
        else:
            present_animals_stack.append(current_animal_event)
    
    else:
        animal_to_exit = -current_animal_event
        
        if animal_to_exit in present_animals_stack:
            if animal_to_exit == present_animals_stack[-1]:
                present_animals_stack.remove(animal_to_exit)
            else:
                print(current_event_index + 1)
                break
        else:
            print(current_event_index + 1)
            break
    
    if current_event_index + 1 == number_of_entries:
        print("OK")