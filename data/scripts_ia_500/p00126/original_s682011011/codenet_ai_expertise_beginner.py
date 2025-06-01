import sys

def solve(data):
    status = [[' ' for _ in range(9)] for _ in range(9)]

    # Check rows for duplicates
    for y in range(9):
        freq = {}
        for x in range(9):
            n = data[y][x]
            if n in freq:
                freq[n].append(x)
            else:
                freq[n] = [x]
        for k in freq:
            if len(freq[k]) > 1:
                for x in freq[k]:
                    status[y][x] = '*'

    # Check columns for duplicates
    for x in range(9):
        freq = {}
        for y in range(9):
            n = data[y][x]
            if n in freq:
                freq[n].append(y)
            else:
                freq[n] = [y]
        for k in freq:
            if len(freq[k]) > 1:
                for y in freq[k]:
                    status[y][x] = '*'

    # Check 3x3 blocks for duplicates
    for block_y in range(0, 9, 3):
        for block_x in range(0, 9, 3):
            freq = {}
            for y in range(block_y, block_y+3):
                for x in range(block_x, block_x+3):
                    n = data[y][x]
                    if n in freq:
                        freq[n].append((x, y))
                    else:
                        freq[n] = [(x, y)]
            for k in freq:
                if len(freq[k]) > 1:
                    for (x, y) in freq[k]:
                        status[y][x] = '*'

    # Print result
    for y in range(9):
        line = ''
        for x in range(9):
            line += status[y][x] + str(data[y][x])
        print(line)

def main():
    n = int(sys.stdin.readline())
    for i in range(n):
        data = []
        for _ in range(9):
            row = list(map(int, sys.stdin.readline().split()))
            data.append(row)
        solve(data)
        if i != n - 1:
            print()

if __name__ == '__main__':
    main()