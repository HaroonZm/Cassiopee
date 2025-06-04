import sys

def get_input():
    return input()

def check_end(r):
    if r == "end":
        sys.exit(0)

def check_T(r):
    return r == "T"

def append_chars(s1, s2, sgn1, sgn2, idx):
    s1 += sgn1[idx]
    s2 += sgn2[idx]
    return s1, s2

def remove_last_chars(s1, s2):
    s1 = s1[:-1]
    s2 = s2[:-1]
    return s1, s2

def prepend_chars(s1, s2, sgn1, sgn2, idx):
    s1 = sgn1[idx] + s1
    s2 = sgn2[idx] + s2
    return s1, s2

def remove_first_chars(s1, s2):
    s1 = s1[1:]
    s2 = s2[1:]
    return s1, s2

def print_state(s1, s2):
    print(s1 + "\n" + s2)

def process_forward(s1, s2, sgn1, sgn2):
    for i in range(4):
        s1, s2 = append_chars(s1, s2, sgn1, sgn2, i)
        print_state(s1, s2)
        r = get_input()
        check_end(r)
        if check_T(r):
            return s1, s2, False
        else:
            s1, s2 = remove_last_chars(s1, s2)
    return s1, s2, True

def process_backward(s1, s2, sgn1, sgn2):
    for i in range(4):
        s1, s2 = prepend_chars(s1, s2, sgn1, sgn2, i)
        print_state(s1, s2)
        r = get_input()
        check_end(r)
        if check_T(r):
            break
        else:
            s1, s2 = remove_first_chars(s1, s2)
    return s1, s2

def main_loop(N):
    s1 = ""
    s2 = ""
    sgn1 = "..##"
    sgn2 = ".#.#"
    flag = False
    while True:
        if not flag:
            s1, s2, flag = process_forward(s1, s2, sgn1, sgn2)
        if flag:
            s1, s2 = process_backward(s1, s2, sgn1, sgn2)

def main():
    N = int(input())
    main_loop(N)

main()