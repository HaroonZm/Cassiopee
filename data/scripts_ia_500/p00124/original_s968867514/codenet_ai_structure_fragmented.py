import sys

def read_integer():
    return int(input())

def read_match_result():
    return input().split()

def calculate_value(win, draw):
    return 3 * int(win) + int(draw)

def create_info(name, index, value):
    return Info(name, index, value)

def sort_table(table):
    table.sort()

def print_table(table):
    for info in table:
        print("%s,%d" % (info.name, info.value))

def process_single_table(N):
    table = []
    for i in range(N):
        tmp_name, win, lose, draw = read_match_result()
        value = calculate_value(win, draw)
        info = create_info(tmp_name, i, value)
        table.append(info)
    sort_table(table)
    print_table(table)

def should_break(N):
    return N == 0

def print_newline_if_needed(is_first):
    if not is_first:
        print()

class Info:
    def __init__(self,arg_name,arg_index,arg_value):
        self.name = arg_name
        self.index = arg_index
        self.value = arg_value

    def __lt__(self,another):
        if self.value != another.value:
            return self.value > another.value
        else:
            return self.index < another.index

def main():
    is_First = True
    while True:
        N = read_integer()
        if should_break(N):
            break
        print_newline_if_needed(is_First)
        process_single_table(N)
        is_First = False

if __name__ == "__main__":
    main()