def get_sorting_key_for_end_point(end_point):
    
    value = end_point[0]
    is_start = end_point[1]
    
    if is_start:
        return value * 2 + 1
    else:
        return value * 2


number_of_elements = int(input())

elements = [int(element) for element in input().split()]

elements.append(0)


list_of_end_points = []

current_peak_value = 0

is_ascending = True

for index in range(0, number_of_elements + 1):
    
    if not is_ascending and (index == number_of_elements or elements[index + 1] > elements[index]):
        
        list_of_end_points.append((elements[index], True))
        list_of_end_points.append((current_peak_value, False))
        
        is_ascending = True
        
    elif index != number_of_elements and is_ascending and elements[index + 1] < elements[index]:
        
        current_peak_value = elements[index]
        is_ascending = False


list_of_end_points.sort(key=get_sorting_key_for_end_point)


maximum_overlap_count = 0
current_overlap_count = 0

for end_point in list_of_end_points:
    
    value, is_start = end_point
    
    if is_start:
        
        current_overlap_count += 1
        
        if current_overlap_count > maximum_overlap_count:
            maximum_overlap_count = current_overlap_count
            
    else:
        current_overlap_count -= 1
        
print(maximum_overlap_count)