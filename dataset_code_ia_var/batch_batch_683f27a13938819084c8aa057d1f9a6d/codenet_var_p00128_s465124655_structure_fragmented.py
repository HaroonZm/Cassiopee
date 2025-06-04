def read_input_line():
    try:
        return input()
    except EOFError:
        return None

def input_generator():
    while True:
        inp = read_input_line()
        if inp is None:
            break
        yield ''.join(inp)

def build_table():
    return [
        "* = ****",
        "* =* ***",
        "* =** **",
        "* =*** *",
        "* =**** ",
        " *= ****",
        " *=* ***",
        " *=** **",
        " *=*** *",
        " *=**** "
    ]

def split_inputs(generator):
    return list(generator)

def parse_digit(line, index):
    return int(line[index])

def mod_pow10(power):
    return 10 ** power

def extract_pattern(table, num, i):
    idx = num // mod_pow10(4 - i)
    return table[idx]

def update_num(num, i):
    return num % mod_pow10(4 - i)

def build_ans(table, num):
    ans = []
    for i in range(5):
        pattern = extract_pattern(table, num, i)
        ans.append(pattern)
        num = update_num(num, i)
    return ans

def print_output(ans):
    for i in range(8):
        for j in range(5):
            print(ans[j][i], end="")
        print("")

def print_separator(is_first):
    if not is_first:
        print("")

def process_line(l, N, table):
    print_separator(l == 0)
    num = parse_digit(N, l)
    ans = build_ans(table, num)
    print_output(ans)

def main():
    table = build_table()
    N = split_inputs(input_generator())
    for l in range(len(N)):
        process_line(l, N, table)

main()