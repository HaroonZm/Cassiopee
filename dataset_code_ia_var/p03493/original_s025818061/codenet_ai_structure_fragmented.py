def get_input():
    return input()

def init_counter():
    return 0

def is_one(char):
    return char == "1"

def increment(val):
    return val + 1

def process_char(s, i, cnt):
    if is_one(s[i]):
        cnt = increment(cnt)
    return cnt

def process_all_chars(s):
    cnt = init_counter()
    cnt = process_char(s, 0, cnt)
    cnt = process_char(s, 1, cnt)
    cnt = process_char(s, 2, cnt)
    return cnt

def print_result(cnt):
    print(cnt)

def main():
    s = get_input()
    cnt = process_all_chars(s)
    print_result(cnt)

main()