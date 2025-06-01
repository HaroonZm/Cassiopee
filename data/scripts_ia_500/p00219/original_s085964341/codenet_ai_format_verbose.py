while True:
    
    number_of_inputs = int(input())
    
    if number_of_inputs == 0:
        break
    
    ice_creams_counter = [0] * 10
    
    for _ in range(number_of_inputs):
        ice_cream_flavor = int(input())
        ice_creams_counter[ice_cream_flavor] += 1
    
    for flavor_index in range(10):
        count_for_flavor = ice_creams_counter[flavor_index]
        
        if count_for_flavor > 0:
            for _ in range(count_for_flavor):
                print("*", end="")
            print()
        else:
            print("-")