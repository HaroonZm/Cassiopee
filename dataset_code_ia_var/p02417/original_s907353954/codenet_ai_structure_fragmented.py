import string
import sys

def read_input():
    return sys.stdin.read()

def init_table(size):
    return [0] * size

def get_english_text():
    return read_input()

def count_for_letter(letter, text):
    count = 0
    for char in text:
        if compare_letters(letter, char):
            count += 1
    return count

def compare_letters(letter, char):
    return letter == char or letter.upper() == char

def update_table_for_letter(table, index, letter, text):
    table[index] = count_for_letter(letter, text)

def update_table(table, text):
    index = 0
    for letter in string.ascii_lowercase:
        update_table_for_letter(table, index, letter, text)
        index += 1

def print_table(table):
    index = 0
    for letter in string.ascii_lowercase:
        print_letter_count(letter, table, index)
        index += 1

def print_letter_count(letter, table, index):
    print("%s : %d" % (letter, table[index]))

def main():
    table = init_table(26)
    text = get_english_text()
    update_table(table, text)
    print_table(table)

main()