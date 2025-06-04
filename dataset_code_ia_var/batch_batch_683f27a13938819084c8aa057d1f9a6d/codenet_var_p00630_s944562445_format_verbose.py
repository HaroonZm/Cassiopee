import re

while True:
    user_input_variable_name, output_format_type = input().split()
    
    if output_format_type == 'X':
        break

    if '_' in output_format_type:
        split_variable_name_parts = user_input_variable_name.split('_')
    else:
        split_variable_name_parts = re.findall(r'[a-z]+|[A-Z][a-z]*', user_input_variable_name)

    if output_format_type == 'D':
        formatted_variable_name = '_'.join(part.lower() for part in split_variable_name_parts)
    else:
        formatted_variable_name = ''.join(part.capitalize() for part in split_variable_name_parts)
        if output_format_type == 'L':
            formatted_variable_name = formatted_variable_name[0].lower() + formatted_variable_name[1:]
    
    print(formatted_variable_name)