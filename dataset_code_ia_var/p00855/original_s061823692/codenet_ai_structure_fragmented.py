import math

def create_input_list(num):
    return [is_initially_prime(i) for i in range(num)]

def is_initially_prime(i):
    if i == 2 or i == 3 or i == 5:
        return True
    if i < 2:
        return False
    if i % 2 == 0 or i % 3 == 0 or i % 5 == 0:
        return False
    return True

def set_initial_values(lst):
    lst[0] = False
    lst[1] = False
    lst[2] = True
    lst[3] = True
    lst[5] = True

def get_sqrt(num):
    return math.sqrt(num)

def execute_sieve(lst, num):
    sqrt = get_sqrt(num)
    max_range = get_start_range(num)
    for serial in range(3, max_range, 2):
        process_serial(lst, serial, num, sqrt)
    return lst

def get_start_range(num):
    return num

def process_serial(lst, serial, num, sqrt):
    if serial >= sqrt:
        return
    mark_multiples(lst, serial, num)

def mark_multiples(lst, serial, num):
    start = serial ** 2
    for s in range(start, num, serial):
        lst[s] = False

def sieve_of_erastosthenes(num):
    lst = create_input_list(num)
    set_initial_values(lst)
    return execute_sieve(lst, num)

def read_input():
    return input()

def parse_int(s):
    return int(s)

def is_zero(k):
    return k == 0

def is_prime(primeTable, k):
    return primeTable[k]

def print_zero():
    print(0)

def process_composite(primeTable, k):
    i = find_next_prime(primeTable, k)
    j = find_prev_prime(primeTable, i)
    print_difference(i, j)

def find_next_prime(primeTable, k):
    i = k
    while not is_prime(primeTable, i):
        i += 1
    return i

def find_prev_prime(primeTable, i):
    j = i - 1
    while not is_prime(primeTable, j):
        j -= 1
    return j

def print_difference(i, j):
    print(i - j)

def main():
    primeTable = sieve_of_erastosthenes(13 * (10 ** 5))
    while True:
        k = parse_int(read_input())
        if is_zero(k):
            break
        if is_prime(primeTable, k):
            print_zero()
        else:
            process_composite(primeTable, k)

if __name__ == '__main__':
    main()