while True:
    
    number_of_inputs = int(input())
    
    if number_of_inputs == 0:
        break
    
    frequency_count = [0] * 10
    
    for _ in range(number_of_inputs):
        digit = int(input())
        frequency_count[digit] += 1
    
    for digit_value in range(10):
        if frequency_count[digit_value] == 0:
            print('-')
        else:
            print('*' * frequency_count[digit_value])