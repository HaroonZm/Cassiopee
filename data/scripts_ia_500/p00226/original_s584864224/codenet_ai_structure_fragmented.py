def read_input():
    return input().split()

def check_termination(a, b):
    return a == b == "0"

def count_exact_matches(a, b):
    count = 0
    for i in range(4):
        if a[i] == b[i]:
            count = increment_count(count)
    return count

def increment_count(count):
    return count + 1

def count_partial_matches(a, b):
    newcount = 0
    for j in range(4):
        if char_in_string(a[j], b):
            newcount = increment_count(newcount)
    return newcount

def char_in_string(char, string):
    return char == string[0] or char == string[1] or char == string[2] or char == string[3]

def print_results(count, newcount):
    print(count, end=" ")
    print(newcount - count)

def main_loop():
    while True:
        a, b = read_input()
        if check_termination(a, b):
            break
        count = count_exact_matches(a, b)
        newcount = count_partial_matches(a, b)
        print_results(count, newcount)

main_loop()