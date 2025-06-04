first_integer, second_integer = map(int, input().split())

if second_integer % first_integer == 0:
    
    print(first_integer + second_integer)
    
else:
    
    print(second_integer - first_integer)