first_number, second_number, third_number = map(int, input().split())

if first_number == second_number and first_number != third_number:
    
    print("Yes")

elif first_number == third_number and second_number != third_number:
    
    print("Yes")

elif third_number == second_number and first_number != third_number:
    
    print("Yes")

else:
    
    print("No")