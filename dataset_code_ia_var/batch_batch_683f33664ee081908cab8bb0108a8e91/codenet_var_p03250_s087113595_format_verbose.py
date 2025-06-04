input_numbers = list(map(int, input().split()))

input_numbers.sort()

largest_number = input_numbers[2]
second_largest_number = input_numbers[1]
smallest_number = input_numbers[0]

result = 10 * largest_number + second_largest_number + smallest_number

print(result)