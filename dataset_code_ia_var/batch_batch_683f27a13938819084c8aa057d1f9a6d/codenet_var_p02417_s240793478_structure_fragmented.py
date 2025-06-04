import sys

def get_chklist():
    return ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def init_word():
    return ''

def read_input():
    return sys.stdin

def accumulate_input(input_iter):
    result = ''
    for i in input_iter:
        result = add_to_word(result, i)
    return result

def add_to_word(current, addition):
    return current + addition

def count_for_letter(letter, word):
    cnt = 0
    for char in word:
        cnt = inc_if_equal(letter, char, cnt)
    return cnt

def inc_if_equal(letter, char, cnt):
    if are_equal_ignore_case(letter, char):
        cnt += 1
    return cnt

def are_equal_ignore_case(a, b):
    return a.upper() == b.upper()

def print_letter_count(letter, cnt):
    print(str.format('{} : {}', letter, cnt))

def main():
    chklist = get_chklist()
    word = init_word()
    input_iter = read_input()
    word = accumulate_input(input_iter)
    for n in chklist:
        cnt = count_for_letter(n, word)
        print_letter_count(n, cnt)

main()