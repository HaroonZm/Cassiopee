def read_input():
    return raw_input()

def get_characters():
    return ['A', 'B', 'C']

def is_length_small(s):
    return len(s) <= 3

def check_abc(s):
    return s == "ABC"

def print_result(result):
    print "Yes" if result else "No"

def split_abc(s):
    return s.strip().split("ABC")

def join_parts(parts):
    return ''.join(parts)

def contains(char, s):
    return char in s

def update_s(x, parts):
    return x.join(parts)

def count_in_chars(chars, p):
    count = 0
    for x in chars:
        if contains(x, p):
            count += 1
    return count

def find_missing(chars, p):
    missing = []
    for x in chars:
        if not contains(x, p):
            missing.append(x)
    return missing

def update_string_if_missing(s, chars, parts):
    for x in chars:
        if not contains(x, ''.join(parts)):
            return update_s(x, parts)
    return s

def process_string(s, chars):
    while True:
        if is_length_small(s):
            print_result(check_abc(s))
            break
        parts = split_abc(s)
        p = join_parts(parts)
        cnt = 0
        for x in chars:
            if contains(x, p):
                cnt += 1
            else:
                s = update_s(x, parts)
        if len(parts) == 1 or cnt != 2:
            print_result(False)
            break

def main():
    s = read_input()
    chars = get_characters()
    process_string(s, chars)

if __name__ == "__main__":
    main()