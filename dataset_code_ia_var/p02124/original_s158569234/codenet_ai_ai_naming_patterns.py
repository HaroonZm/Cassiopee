user_input_value = int(input())
normalized_value = user_input_value / 100

def generate_ai1333_suffix(value):
    if value == 0:
        return 'ai1333'
    else:
        previous_result = generate_ai1333_suffix(value - 1)
        appended_result = previous_result + '3'
        return appended_result

print(generate_ai1333_suffix(normalized_value))