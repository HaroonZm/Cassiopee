first_integer, second_integer = map(int, input().split())

if second_integer % first_integer == 0:
    
    result = first_integer + second_integer
    print(result)

else:
    
    result = second_integer - first_integer
    print(result)