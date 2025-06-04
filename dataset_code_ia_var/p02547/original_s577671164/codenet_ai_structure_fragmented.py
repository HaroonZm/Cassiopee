def get_input():
    return int(input())

def get_pair():
    return tuple(map(int, input().split()))

def is_pair_equal(pair):
    return pair[0] == pair[1]

def increment_counter(counter):
    return counter + 1

def reset_counter():
    return 0

def update_flag(counter, flag):
    if counter == 3:
        return True
    return flag

def process_pairs(n):
    counter = 0
    flag = False
    for _ in range(n):
        pair = get_pair()
        if is_pair_equal(pair):
            counter = increment_counter(counter)
            flag = update_flag(counter, flag)
        else:
            counter = reset_counter()
    return flag

def print_result(flag):
    if flag:
        print("Yes")
    else:
        print("No")

def main():
    n = get_input()
    flag = process_pairs(n)
    print_result(flag)

main()