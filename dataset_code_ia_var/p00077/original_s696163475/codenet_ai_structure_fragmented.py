def read_input():
    return list(input())

def pop_first(lst):
    return lst.pop(0)

def is_at_symbol(ch):
    return ch == "@"

def handle_at_sequence(s):
    c = pop_first(s)
    l = pop_first(s)
    return l * int(c)

def handle_normal_character(i):
    return i

def process_single_step(s, ans):
    i = pop_first(s)
    if is_at_symbol(i):
        ans += handle_at_sequence(s)
    else:
        ans += handle_normal_character(i)
    return s, ans

def process_input(s):
    ans = ""
    while len(s) > 0:
        s, ans = process_single_step(s, ans)
    return ans

def main_loop():
    while True:
        try:
            s = read_input()
            ans = process_input(s)
            print(ans)
        except:
            break

main_loop()