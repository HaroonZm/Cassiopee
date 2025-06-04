def get_input():
    return input()

def to_int(value):
    return int(value)

def parse_list(values):
    return list(map(int, values.split()))

def sort_descending(lst):
    return sorted(lst, reverse=True)

def is_even(number):
    return number % 2 == 0

def assign_player_lists(number_of_elements, lst):
    alice = []
    bob = []
    for i in range(number_of_elements):
        if is_even(i):
            append_to_list(alice, lst[i])
        else:
            append_to_list(bob, lst[i])
    return alice, bob

def append_to_list(lst, value):
    lst.append(value)

def sum_list(lst):
    return sum(lst)

def print_result(result):
    print(result)

def main():
    n = to_int(get_input())
    raw_list = get_input()
    input_list = parse_list(raw_list)
    sorted_list = sort_descending(input_list)
    alice_list, bob_list = assign_player_lists(n, sorted_list)
    alice_sum = sum_list(alice_list)
    bob_sum = sum_list(bob_list)
    result = alice_sum - bob_sum
    print_result(result)

main()