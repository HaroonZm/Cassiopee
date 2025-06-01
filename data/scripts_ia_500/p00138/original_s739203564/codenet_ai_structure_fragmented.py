def read_line():
    return raw_input()

def read_eight_lines():
    return [read_line() for _ in [0]*8]

def read_three_blocks():
    return [read_eight_lines() for _ in [0]*3]

def sort_block(e):
    return sorted(e, key=lambda x: x.split()[1])

def get_top_two(b):
    return b[:2]

def get_third_and_fourth(b):
    return b[2:4]

def print_lines(lines):
    print '\n'.join(lines)

def process_block(e):
    b = sort_block(e)
    print_lines(get_top_two(b))
    return get_third_and_fourth(b)

def main():
    x = []
    blocks = read_three_blocks()
    blocks.append(x)
    for e in blocks:
        added = process_block(e)
        x += added

main()