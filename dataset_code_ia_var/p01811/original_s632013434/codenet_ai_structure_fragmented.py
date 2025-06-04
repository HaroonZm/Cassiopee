def get_input():
    return input()

def get_end_string():
    return "ABC"

def should_continue(s, end):
    return s != end

def print_yes():
    print("Yes")

def print_no():
    print("No")

def replace_ABC_with_X(s):
    return s.replace("ABC", "X")

def check_X_not_in_s(s):
    return "X" not in s

def count_ABC_in_s(s):
    return ("A" in s) + ("B" in s) + ("C" in s)

def need_to_stop(s):
    return check_X_not_in_s(s) or count_ABC_in_s(s) != 2

def missing_ABC_char(s):
    for c in "ABC":
        if c not in s:
            return c
    return None

def replace_X_with_missing(s):
    missing = missing_ABC_char(s)
    if missing is not None:
        return s.replace("X", missing)
    return s

def main_loop(s, end):
    while True:
        if not should_continue(s, end):
            print_yes()
            break
        s = replace_ABC_with_X(s)
        if need_to_stop(s):
            print_no()
            break
        s = replace_X_with_missing(s)

def main():
    s = get_input()
    end = get_end_string()
    main_loop(s, end)

main()