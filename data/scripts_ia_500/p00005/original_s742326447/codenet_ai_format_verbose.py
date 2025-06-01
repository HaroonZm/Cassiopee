import sys

def read_integers_from_input():
    
    input_line = input()
    
    string_elements = input_line.split()
    
    integer_elements = []
    
    for element in string_elements:
        
        integer_elements.append(int(element))
    
    return integer_elements


def calculate_gcd(first_number, second_number):
    
    if first_number < second_number:
        
        return calculate_gcd(second_number, first_number)
    
    if second_number == 0:
        
        return first_number
    
    return calculate_gcd(second_number, first_number % second_number)


def main():
    
    all_input_lines = sys.stdin.readlines()
    
    data_pairs = []
    
    for line in all_input_lines:
        
        split_line = line.split()
        
        data_pairs.append(split_line)
    
    total_pairs = len(data_pairs)
    
    for index in range(total_pairs):
        
        first_value = int(data_pairs[index][0])
        
        second_value = int(data_pairs[index][1])
        
        gcd_value = calculate_gcd(first_value, second_value)
        
        lcm_value = (first_value // gcd_value) * second_value
        
        print('%d %d' % (gcd_value, lcm_value))


if __name__ == "__main__":
    
    main()