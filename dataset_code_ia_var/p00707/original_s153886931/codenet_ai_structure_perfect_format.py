def isValid(row, col, ROWS, COLS):
    return row >= 0 and row < ROWS and col >= 0 and col < COLS

def search(matrix, row, col, ROWS, COLS, memo):
    if (row, col) in memo:
        return memo[(row, col)]

    numStrA = ''
    numStrB = ''

    rr = row + 1
    cc = col
    if isValid(rr, cc, ROWS, COLS) and matrix[rr][cc].isdigit():
        numStrA = search(matrix, rr, cc, ROWS, COLS, memo)

    rr = row
    cc = col + 1
    if isValid(rr, cc, ROWS, COLS) and matrix[rr][cc].isdigit():
        numStrB = search(matrix, rr, cc, ROWS, COLS, memo)

    numStrA = matrix[row][col] + numStrA
    numStrB = matrix[row][col] + numStrB

    if len(numStrA) > len(numStrB):
        val = numStrA
    elif len(numStrB) > len(numStrA):
        val = numStrB
    else:
        if numStrA > numStrB:
            val = numStrA
        else:
            val = numStrB

    memo[(row, col)] = val
    return val

if __name__ == '__main__':
    while True:
        COLS, ROWS = [int(x) for x in filter(lambda x: x != '', input().strip().split(' '))]
        if ROWS == 0 and COLS == 0:
            break

        matrix = []
        for _ in range(ROWS):
            matrix.append(input().strip())

        maxNum = 0
        memo = {}
        for row in range(ROWS):
            for col in range(COLS):
                if matrix[row][col].isdigit() and matrix[row][col] != '0':
                    maxNum = max(maxNum, int(search(matrix, row, col, ROWS, COLS, memo)))

        print(maxNum)