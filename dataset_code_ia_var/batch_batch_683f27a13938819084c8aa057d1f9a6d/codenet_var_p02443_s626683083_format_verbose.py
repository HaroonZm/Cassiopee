number_of_elements = int(input())

integer_list = list(map(int, input().split()))

number_of_operations = int(input())

for operation_index in range(number_of_operations):
    
    start_index, end_index = map(int, input().split())
    
    integer_list[start_index:end_index] = reversed(integer_list[start_index:end_index])

print(*integer_list)