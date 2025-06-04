number_of_queries = int(input())

key_value_store = {}

for query_index in range(number_of_queries):
    
    user_input = input().split()
    operation_code = user_input[0]
    
    if operation_code == "0":
        
        key_to_insert = user_input[1]
        value_to_insert = user_input[2]
        key_value_store[key_to_insert] = value_to_insert

    elif operation_code == "1":
        
        key_to_lookup = user_input[1]
        if key_to_lookup in key_value_store:
            print(key_value_store[key_to_lookup])
        else:
            print(0)

    elif operation_code == "2":
        
        key_to_delete = user_input[1]
        if key_to_delete in key_value_store:
            del key_value_store[key_to_delete]