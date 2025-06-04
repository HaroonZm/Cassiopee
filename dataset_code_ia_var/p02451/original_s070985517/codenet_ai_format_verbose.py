from bisect import bisect_left

number_of_elements = int(input())

sorted_integer_list = list(map(int, input().split()))

sorted_integer_list.append(1000000001)  # Ajoute une valeur sentinelle plus grande que les entrées possibles

number_of_queries = int(input())

for query_index in range(number_of_queries):
    
    target_value = int(input())
    
    insertion_index = bisect_left(sorted_integer_list, target_value)
    
    if sorted_integer_list[insertion_index] == target_value:
        print(1)
    else:
        print(0)