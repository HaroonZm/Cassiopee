def is_valid(row, col, ROWS, COLS):
    if row < 0 or row >= ROWS:
        return False
    if col < 0 or col >= COLS:
        return False
    return True

def search(matrix, row, col, ROWS, COLS, memo):
    if (row, col) in memo:
        return memo[(row, col)]
    string_a = ''
    string_b = ''
    new_row = row + 1
    new_col = col
    if is_valid(new_row, new_col, ROWS, COLS):
        if matrix[new_row][new_col].isdigit():
            string_a = search(matrix, new_row, new_col, ROWS, COLS, memo)
    new_row = row
    new_col = col + 1
    if is_valid(new_row, new_col, ROWS, COLS):
        if matrix[new_row][new_col].isdigit():
            string_b = search(matrix, new_row, new_col, ROWS, COLS, memo)
    string_a = matrix[row][col] + string_a
    string_b = matrix[row][col] + string_b
    if len(string_a) > len(string_b):
        result = string_a
    elif len(string_b) > len(string_a):
        result = string_b
    else:
        if string_a > string_b:
            result = string_a
        else:
            result = string_b
    memo[(row, col)] = result
    return result

if __name__ == '__main__':
    while True:
        nums = input().strip().split(' ')
        temp = []
        for item in nums:
            if item != '':
                temp.append(int(item))
        if len(temp) != 2:
            continue
        COLS = temp[0]
        ROWS = temp[1]
        if ROWS == 0 and COLS == 0:
            break
        matrix = []
        for _ in range(ROWS):
            matrix.append(input().strip())
        max_num = 0
        memo = {}
        for row in range(ROWS):
            for col in range(COLS):
                if matrix[row][col].isdigit() and matrix[row][col] != '0':
                    find_num = int(search(matrix, row, col, ROWS, COLS, memo))
                    if find_num > max_num:
                        max_num = find_num
        print(max_num)