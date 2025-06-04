import math

number_of_elements = int(input())

unsorted_integer_list = [int(element) for element in input().split()]

sorted_integer_list = sorted(unsorted_integer_list)

current_gcd = sorted_integer_list[0]

for index in range(1, number_of_elements):
    
    current_gcd = math.gcd(current_gcd, sorted_integer_list[index])
    
    if current_gcd == 1:
        break

print(current_gcd)