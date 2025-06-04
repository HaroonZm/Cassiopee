import sys

for input_line in sys.stdin:
    
    user_input_integer = int(input_line)
    
    minimum_required_value = 30
    
    if user_input_integer >= minimum_required_value:
        print("Yes")
    else:
        print("No")