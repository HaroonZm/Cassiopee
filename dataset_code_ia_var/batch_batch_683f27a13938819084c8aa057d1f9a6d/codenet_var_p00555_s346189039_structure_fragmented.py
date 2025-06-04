def read_input_values():
    return map(int, input().split())

def read_field_rows(n):
    rows = []
    for _ in range(n):
        rows.append(input())
    return rows

def split_row_on_hash(row):
    return row.split("#")

def count_valid_sequences_in_split(split_list, d):
    count = 0
    for seq in split_list:
        count += count_valid_sequences_in_string(seq, d)
    return count

def count_valid_sequences_in_string(s, d):
    if len(s) >= d:
        return len(s) - d + 1
    return 0

def process_rows(rows, d):
    total = 0
    for row in rows:
        split_list = split_row_on_hash(row)
        total += count_valid_sequences_in_split(split_list, d)
    return total

def transpose_field(field):
    transposed = [list(x) for x in zip(*field)]
    return transposed

def join_transposed_rows(transposed):
    joined = []
    for row in transposed:
        joined.append("".join(map(str, row)))
    return joined

def main():
    n, m, d = read_input_values()
    field = read_field_rows(n)
    total_ans = 0
    total_ans += process_rows(field, d)
    field_t = transpose_field(field)
    field_t = join_transposed_rows(field_t)
    total_ans += process_rows(field_t, d)
    print(total_ans)

main()