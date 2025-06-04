user_input_as_string_list = list(map(str, input().split()))

unique_numbers_in_input = set(user_input_as_string_list)

required_numbers = {'1', '9', '7', '4'}

if all(number in unique_numbers_in_input for number in required_numbers):
    
    print("YES")

else:
    
    print("NO")