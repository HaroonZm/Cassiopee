def get_abacus_references():
    return ["= ****", "=* ***", "=** **", "=*** *", "=**** "]

def pad_left_with_zeros(s, total_length):
    return "0" * (total_length - len(s)) + s

def initialize_abacus(size):
    return ["" for _ in range(size)]

def get_single_abacus_row(digit, ref):
    if int(digit) < 5:
        row = "* "
    else:
        row = " *"
    row += ref[int(digit) % 5]
    return row

def fill_abacus_rows(n, ref):
    abacus = initialize_abacus(5)
    for i in range(4, -1, -1):
        abacus[i] += get_single_abacus_row(n[i], ref)
    return abacus

def get_abacus_column(abacus, col_index):
    column = ""
    for row in abacus:
        column += row[col_index]
    return column

def print_abacus(abacus):
    for i in range(8):
        print(get_abacus_column(abacus, i))

def process_input(n, ref):
    n = pad_left_with_zeros(n, 5)
    abacus = fill_abacus_rows(n, ref)
    print_abacus(abacus)

def abacus_input_loop():
    ref = get_abacus_references()
    try:
        n = raw_input()
    except:
        return
    while True:
        try:
            process_input(n, ref)
            try:
                n = raw_input()
            except:
                break
            print
        except:
            break

abacus_input_loop()