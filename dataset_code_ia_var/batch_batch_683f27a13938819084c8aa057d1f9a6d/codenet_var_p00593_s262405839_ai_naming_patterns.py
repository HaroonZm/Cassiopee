def main():
    case_index = 1
    while True:
        matrix_size = int(input())
        if matrix_size == 0:
            break

        matrix = [ [0 for _ in range(matrix_size)] for _ in range(matrix_size) ]

        row_index = 0
        col_index = 0
        current_value = 1
        last_move = "UP_RIGHT"

        while True:
            matrix[row_index][col_index] = current_value
            current_value += 1

            if row_index == matrix_size - 1 and col_index == matrix_size - 1:
                break
            elif row_index == 0:
                if last_move == "UP_RIGHT":
                    if col_index != matrix_size - 1:
                        col_index += 1
                        last_move = "RIGHT"
                    else:
                        row_index += 1
                        last_move = "DOWN"
                else:
                    row_index += 1
                    col_index -= 1
                    last_move = "DOWN_LEFT"
            elif row_index == matrix_size - 1:
                if last_move == "DOWN_LEFT":
                    col_index += 1
                    last_move = "RIGHT"
                else:
                    row_index -= 1
                    col_index += 1
                    last_move = "UP_RIGHT"
            elif col_index == 0:
                if last_move == "DOWN_LEFT":
                    row_index += 1
                    last_move = "DOWN"
                else:
                    row_index -= 1
                    col_index += 1
                    last_move = "UP_RIGHT"
            elif col_index == matrix_size - 1:
                if last_move == "UP_RIGHT":
                    row_index += 1
                    last_move = "DOWN"
                else:
                    row_index += 1
                    col_index -= 1
                    last_move = "DOWN_LEFT"
            else:
                if last_move == "DOWN_LEFT":
                    row_index += 1
                    col_index -= 1
                else:
                    row_index -= 1
                    col_index += 1

        print("Case {}:".format(case_index))
        case_index += 1

        for output_row_index in range(matrix_size):
            for output_col_index in range(matrix_size):
                print("{:3d}".format(matrix[output_row_index][output_col_index]), end='')
            print()

if __name__ == '__main__':
    main()