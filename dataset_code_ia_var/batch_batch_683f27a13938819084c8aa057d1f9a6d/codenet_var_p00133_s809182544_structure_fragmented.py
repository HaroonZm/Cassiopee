import sys

def get_input_line():
    return list(raw_input())

def append_to_ptn(ptn, line):
    ptn.append(line)

def read_pattern_lines():
    lines = []
    for i in range(8):
        line = get_input_line()
        append_to_ptn(lines, line)
    return lines

def get_column(ptn, col_idx):
    return [row[col_idx] for row in ptn]

def zip_columns(ptn):
    cols = []
    for i in range(8):
        cols.append(get_column(ptn, i))
    return cols

def to_list_cols(zipped):
    listed = []
    for col in zipped:
        listed.append(list(col))
    return listed

def reverse_row(row):
    row.reverse()
    return row

def reverse_all_rows(rows):
    result = []
    for row in rows:
        result.append(reverse_row(row))
    return result

def rotate90(ptn):
    zipped = zip_columns(ptn)
    listed = to_list_cols(zipped)
    reversed_rows = reverse_all_rows(listed)
    return reversed_rows

def prepare_stdout_write_element(element):
    sys.stdout.write(element)

def prepare_stdout_write_row(row):
    for element in row:
        prepare_stdout_write_element(element)

def prepare_stdout_write_newline():
    print

def print_ptn_row(row):
    prepare_stdout_write_row(row)
    prepare_stdout_write_newline()

def print_ptn(ptn):
    for row in ptn:
        print_ptn_row(row)

def get_rotation_label(i):
    return 90 * (i + 1)

def print_rotation_label(label):
    print label

def rotate_and_print(ptn, times):
    for i in range(times):
        label = get_rotation_label(i)
        print_rotation_label(label)
        ptn = rotate90(ptn)
        print_ptn(ptn)
    return ptn

def main():
    ptn = read_pattern_lines()
    rotate_and_print(ptn, 3)

main()