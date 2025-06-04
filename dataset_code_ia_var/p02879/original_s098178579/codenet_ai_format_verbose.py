def calculate_product_of_single_digit_integers():
    first_integer, second_integer = map(int, input().split())
    
    if 1 <= first_integer <= 9 and 1 <= second_integer <= 9:
        return first_integer * second_integer
    else:
        return -1

if __name__ == '__main__':
    print(calculate_product_of_single_digit_integers())