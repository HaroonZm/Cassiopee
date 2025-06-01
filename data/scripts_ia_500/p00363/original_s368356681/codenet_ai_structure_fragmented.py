def read_input():
    w, h, c = input().split()
    return int(w), int(h), c

def initialize_strings():
    return "", "", ""

def increment_counter(counter):
    return counter + 1

def build_strings(w, c):
    a, d, d_e = initialize_strings()
    cnt = 2
    for i in range(w - 2):
        cnt = increment_counter(cnt)
        a = append_char(a, "-")
        d = append_char(d, ".")
        d_e = append_d_e(cnt, w, d_e, c)
    return a, d, d_e

def append_char(s, char):
    return s + char

def append_d_e(cnt, w, d_e, c):
    if cnt != w // 2 + 2:
        d_e += "."
    else:
        d_e += c
    return d_e

def print_top_bottom(a):
    print("+" + a + "+")

def print_middle_rows(h, d, d_e):
    cnt = 2
    for j in range(h - 2):
        cnt = increment_counter(cnt)
        line = build_line(cnt, h, d, d_e)
        print(line)

def build_line(cnt, h, d, d_e):
    if cnt != h // 2 + 2:
        return "|" + d + "|"
    else:
        return "|" + d_e + "|"

def main():
    w, h, c = read_input()
    a, d, d_e = build_strings(w, c)
    print_top_bottom(a)
    print_middle_rows(h, d, d_e)
    print_top_bottom(a)

main()