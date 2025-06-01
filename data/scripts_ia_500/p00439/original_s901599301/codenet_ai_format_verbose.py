def solve():
    
    while True:
        number_of_elements, subarray_length = [int(value) for value in input().split()]
        
        if number_of_elements == 0:
            return
        
        elements = [int(input()) for _ in range(number_of_elements)]
        
        prefix_sums = [0] * (number_of_elements + 1)
        
        for index in range(number_of_elements):
            prefix_sums[index + 1] = prefix_sums[index] + elements[index]
        
        maximum_subarray_sum = -1
        
        for start_index in range(number_of_elements):
            end_index = start_index + subarray_length
            
            if end_index > number_of_elements:
                break
            
            current_subarray_sum = prefix_sums[end_index] - prefix_sums[start_index]
            if current_subarray_sum > maximum_subarray_sum:
                maximum_subarray_sum = current_subarray_sum
        
        print(maximum_subarray_sum)

if __name__ == '__main__':
    solve()