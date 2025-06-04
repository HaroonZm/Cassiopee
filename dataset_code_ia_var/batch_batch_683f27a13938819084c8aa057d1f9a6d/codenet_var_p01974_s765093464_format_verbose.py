import itertools

number_of_elements = int(input())

list_of_integers = list(map(int, input().split()))

for integer_pair in itertools.combinations(list_of_integers, 2):

    absolute_difference = abs(integer_pair[0] - integer_pair[1])
    
    if absolute_difference % (number_of_elements - 1) == 0:
    
        print(integer_pair[0], integer_pair[1])
        
        break