number_of_elements = int(input())

input_numbers = list(map(int, input().split()))

sorted_numbers_descending = sorted(input_numbers, reverse=True)

maximum_number = sorted_numbers_descending[0]

half_of_maximum = maximum_number / 2

closest_to_half = sorted_numbers_descending[1]

for index in range(1, number_of_elements):
    
    current_difference = abs(half_of_maximum - sorted_numbers_descending[index])
    closest_difference = abs(half_of_maximum - closest_to_half)

    if current_difference < closest_difference:
        closest_to_half = sorted_numbers_descending[index]

print(maximum_number, closest_to_half)