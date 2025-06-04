import sys

def main():
    number_of_elements = int(sys.stdin.readline().rstrip())
    
    input_values = sys.stdin.readline().rstrip().split()
    integer_list = [int(value) for value in input_values]
    
    integer_list.sort(reverse=True)
    
    duplicated_sorted_list = []
    
    # Duplication of the largest elements (used for the calculation below)
    for index in range((number_of_elements // 2) + 1):
        duplicated_sorted_list.append(integer_list[index])
        duplicated_sorted_list.append(integer_list[index])
    
    # Zeroing the first value as per original logic
    duplicated_sorted_list[0] = 0
    
    result_sum = sum(duplicated_sorted_list[:number_of_elements])
    
    print(result_sum)

main()