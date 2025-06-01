def read_number_of_iterations():
    return int(input())

def initialize_n():
    return 10 ** 2

def update_n(n):
    n = float(n) * 1.05
    return n

def round_up_if_needed(n):
    if n - int(n) > 0:
        n = int(n) + 1
    else:
        n = int(n)
    return n

def multiply_n_by_thousand(n):
    return n * (10 ** 3)

def main():
    n = initialize_n()
    iterations = read_number_of_iterations()
    for _ in range(iterations):
        n = update_n(n)
        n = round_up_if_needed(n)
    result = multiply_n_by_thousand(n)
    print(result)

main()