def get_input():
    return int(input())

def get_denominations():
    return [10000, 5000, 1000, 500]

def get_denominations_length(denominations):
    return len(denominations)

def get_element_from_list(lst, index):
    return lst[index]

def integer_division(a, b):
    return a // b

def multiply(a, b):
    return a * b

def modulo(a, b):
    return a % b

def increment(a, b):
    return a + b

def print_result(result):
    print(result)

def process_denomination(current_n, denomination):
    times = integer_division(current_n, denomination)
    total = multiply(times, denomination)
    remainder = modulo(current_n, denomination)
    return total, remainder

def process_all_denominations(n, denominations):
    ans = 0
    current_n = n
    denominations_length = get_denominations_length(denominations)
    for i in range(denominations_length):
        denomination = get_element_from_list(denominations, i)
        total, remainder = process_denomination(current_n, denomination)
        ans = increment(ans, total)
        current_n = remainder
    return ans

def main():
    n = get_input()
    denominations = get_denominations()
    ans = process_all_denominations(n, denominations)
    print_result(ans)

main()