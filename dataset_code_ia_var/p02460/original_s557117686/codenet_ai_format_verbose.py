number_of_operations = int(input())

variable_storage = {}

for _ in range(number_of_operations):
    
    operation_input = input().split()
    
    operation_type = operation_input[0]
    variable_name = operation_input[1]
    
    if operation_type == "0":
        variable_value = operation_input[2]
        variable_storage[variable_name] = variable_value
    
    elif operation_type == "2":
        variable_storage[variable_name] = 0
    
    else:
        if variable_name in variable_storage:
            print(variable_storage[variable_name])
        else:
            print(0)