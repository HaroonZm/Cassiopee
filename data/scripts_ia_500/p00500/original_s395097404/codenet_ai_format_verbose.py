list_of_triplets = []

number_of_triplets = int(raw_input())

for _ in range(number_of_triplets):
    
    triplet_strings = raw_input().split()
    
    triplet_integers = map(int, triplet_strings)
    
    list_of_triplets.append(triplet_integers)

for current_index in range(number_of_triplets):
    
    flags_for_unique_elements = [1, 1, 1]
    
    for comparison_index in range(number_of_triplets):
        
        if current_index == comparison_index:
            continue
        
        for element_index in range(3):
            
            current_element = list_of_triplets[current_index][element_index]
            
            comparison_element = list_of_triplets[comparison_index][element_index]
            
            if current_element == comparison_element:
                
                flags_for_unique_elements[element_index] = 0
    
    result_sum = (list_of_triplets[current_index][0] * flags_for_unique_elements[0] + 
                  list_of_triplets[current_index][1] * flags_for_unique_elements[1] + 
                  list_of_triplets[current_index][2] * flags_for_unique_elements[2])
    
    print result_sum