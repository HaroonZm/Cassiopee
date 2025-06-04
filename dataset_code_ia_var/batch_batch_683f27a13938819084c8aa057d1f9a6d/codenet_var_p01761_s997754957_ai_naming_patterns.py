import sys

def read_int():
    return int(sys.stdin.readline())

def read_line():
    return sys.stdin.readline().strip().split()

def prefix_star(value):
    return '*' + value

def process_data_rows(num_rows):
    rows = []
    for row_idx in range(num_rows):
        value1, value2, value3 = read_line()
        row = [prefix_star(value1), prefix_star(value2), value3]
        rows.append(row)
    return rows

def process_query_block(num_queries, data_rows):
    for query_idx in range(num_queries):
        query_beg, query_act, filt_min, filt_max = read_line()
        filt_max_val = '9*' if filt_max == '*' else filt_max
        for data_beg, data_act, data_fil in data_rows:
            if query_beg in data_beg and query_act in data_act and filt_min <= data_fil <= filt_max_val:
                print(data_beg[1:])
        if query_idx < num_queries - 1:
            print()

def main():
    total_rows = read_int()
    data_matrix = process_data_rows(total_rows)
    total_queries = read_int()
    process_query_block(total_queries, data_matrix)

if __name__ == "__main__":
    main()