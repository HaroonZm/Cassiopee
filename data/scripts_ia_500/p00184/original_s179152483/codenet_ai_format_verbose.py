while True:
    
    number_of_inputs = int(input())
    
    if number_of_inputs == 0:
        break
    
    height_bins = [0, 0, 0, 0, 0, 0, 0]
    
    for _ in range(number_of_inputs):
        
        input_height = int(input())
        
        height_category = input_height // 10
        
        if height_category > 6:
            height_category = 6
        
        height_bins[height_category] += 1
    
    for bin_index in range(7):
        print(height_bins[bin_index])