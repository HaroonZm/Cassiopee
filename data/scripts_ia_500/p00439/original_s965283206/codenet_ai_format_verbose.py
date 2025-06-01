def calculate_maximum_sum_subarray():
    
    for _ in range(5):
        
        array_length, subarray_size = map(int, input().split())
        
        if array_length == 0 and subarray_size == 0:
            break
        
        elements = [int(input()) for _ in range(array_length)]
        
        current_subarray_sum = 0
        maximum_subarray_sum = 0
        
        for index, element in enumerate(elements):
            
            if 0 <= index <= subarray_size - 1:
                current_subarray_sum += element
            
            else:
                current_subarray_sum = current_subarray_sum + element - elements[index - subarray_size]
                
                if current_subarray_sum > maximum_subarray_sum:
                    maximum_subarray_sum = current_subarray_sum
        
        print(maximum_subarray_sum)