def main():
    while True:
        input_line = input()
        if input_line == '0 0':
            break
        row_count = int(input_line.split()[0])
        matrix_rows = [input().split() for _ in range(row_count)]
        transposed_bits = zip(*matrix_rows)
        column_values = [int(''.join(bits), 2) for bits in transposed_bits]
        max_score = 0
        limit = 1 << (row_count - 1)
        for mask in range(limit):
            current_score = 0
            for value in column_values:
                diff_bits = bin(mask ^ value).count('1')
                if diff_bits > row_count // 2:
                    current_score += diff_bits
                else:
                    current_score += row_count - diff_bits
            if current_score > max_score:
                max_score = current_score
        print(max_score)

if __name__ == '__main__':
    main()