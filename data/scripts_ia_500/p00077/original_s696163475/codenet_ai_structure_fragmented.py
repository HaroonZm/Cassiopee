def read_input():
    return list(input())

def process_input(s):
    ans = ""
    while len(s) > 0:
        i = pop_first_char(s)
        ans = handle_char(i, s, ans)
    return ans

def pop_first_char(s):
    return s.pop(0)

def handle_char(i, s, ans):
    if i == "@":
        c = pop_first_char(s)
        l = pop_first_char(s)
        ans = repeat_and_add(ans, c, l)
    else:
        ans = add_char(ans, i)
    return ans

def repeat_and_add(ans, c, l):
    return ans + l * int(c)

def add_char(ans, i):
    return ans + i

def main():
    while True:
        try:
            s = read_input()
            ans = process_input(s)
            print(ans)
        except:
            break

main()