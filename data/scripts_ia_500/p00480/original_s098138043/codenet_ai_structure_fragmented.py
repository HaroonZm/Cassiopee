def input_integer():
    return int(input())

def input_number_list():
    return [int(i) for i in input().split(" ")]

def pop_last_element(lst):
    return lst.pop(-1)

def should_pop_first_zero(lst):
    return lst[0] == 0

def decrement(value):
    return value - 1

def pop_first_element(lst):
    return lst.pop(0)

def initialize_numbermap(rows, cols):
    return [[0 for _ in range(cols)] for _ in range(rows)]

def set_first_element(numbermap):
    numbermap[0][0] = 1

def can_add(j, num):
    return j + num <= 20

def can_subtract(j, num):
    return j - num >= 0

def update_numbermap_plus(numbermap, i, j, num):
    numbermap[i+1][j+num] += numbermap[i][j]

def update_numbermap_minus(numbermap, i, j, num):
    numbermap[i+1][j-num] += numbermap[i][j]

def process_numbermap(numbermap, number, N):
    for i in range(N-1):
        for j in range(21):
            process_position(numbermap, i, j, number)
            
def process_position(numbermap, i, j, number):
    if can_add(j, number[i]):
        update_numbermap_plus(numbermap, i, j, number[i])
    if can_subtract(j, number[i]):
        update_numbermap_minus(numbermap, i, j, number[i])

def print_result(numbermap, a):
    print(numbermap[-1][a])

def main():
    N = input_integer()
    number = input_number_list()
    a = pop_last_element(number)

    if should_pop_first_zero(number):
        N = decrement(N)
        pop_first_element(number)

    numbermap = initialize_numbermap(N, 21)
    set_first_element(numbermap)

    process_numbermap(numbermap, number, N)

    print_result(numbermap, a)

main()