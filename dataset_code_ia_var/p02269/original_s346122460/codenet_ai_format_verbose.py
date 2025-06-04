from collections import deque

set_of_strings = set()

number_of_operations = int(input())

for operation_index in range(number_of_operations):
    
    command, string_value = input().split()
    
    if command == "insert":
        set_of_strings.add(string_value)
        
    elif command == "find":
        if string_value in set_of_strings:
            print("yes")
        else:
            print("no")