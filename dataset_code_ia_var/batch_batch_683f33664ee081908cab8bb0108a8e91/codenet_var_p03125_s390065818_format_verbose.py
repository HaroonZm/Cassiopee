# AtCoder problem rewritten with explicit variable names and spaced structure

first_integer_input, second_integer_input = map(int, input().split())

if second_integer_input % first_integer_input == 0:
    
    sum_of_integers = first_integer_input + second_integer_input
    print(sum_of_integers)

else:
    
    difference_of_integers = second_integer_input - first_integer_input
    print(difference_of_integers)