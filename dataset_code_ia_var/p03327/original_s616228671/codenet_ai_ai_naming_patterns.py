user_input_value = int(input(' '))

def category_label_from_number(number_value):
    if number_value <= 999:
        return 'ABC'
    else:
        return 'ABD'

print(category_label_from_number(user_input_value))