while True:
    
    number_of_inputs = int(input())
    
    if number_of_inputs == 0:
        break
    
    input_numbers = [int(input()) for _ in range(number_of_inputs)]
    
    frequency_counts = [0 for _ in range(10)]
    
    for number in input_numbers:
        frequency_counts[number] += 1
    
    for digit in range(10):
        count = frequency_counts[digit]
        if count == 0:
            print('-')
        else:
            print('*' * count)