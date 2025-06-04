input_count = int(input())
input_numbers = [int(number_str) for number_str in input().split()]

max_number = max(input_numbers)
sum_numbers = sum(input_numbers)
is_valid = max_number < (sum_numbers - max_number)

print("Yes" if is_valid else "No")