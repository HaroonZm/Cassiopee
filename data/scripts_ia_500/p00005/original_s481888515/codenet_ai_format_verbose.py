def compute_gcd(first_number: int, second_number: int) -> int:
    
    if second_number == 0:
        return first_number
    
    return compute_gcd(second_number, first_number % second_number)


def main():
    
    while True:
        try:
            input_numbers = list(map(int, input().split()))
            
            first_input_number = input_numbers[0]
            second_input_number = input_numbers[1]
            
            greatest_common_divisor = compute_gcd(first_input_number, second_input_number)
            
            least_common_multiple = first_input_number // greatest_common_divisor * second_input_number
            
            print(f'{greatest_common_divisor} {least_common_multiple}')
        
        except Exception:
            break


if __name__ == "__main__":
    main()