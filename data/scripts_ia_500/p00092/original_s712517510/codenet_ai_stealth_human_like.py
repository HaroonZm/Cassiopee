import sys

def largest_square(grid):
    # convert grid to 0/1 map where '.' is 1, others 0
    dp_map = []
    for line in grid:
        row_data = []
        for char in line:
            if char == '.':
                row_data.append(1)
            else:
                row_data.append(0)
        dp_map.append(row_data)

    max_square = 0
    prev = dp_map[0]
    for curr in dp_map[1:]:
        for i in range(1, len(curr)):
            if curr[i] == 1:
                # update current cell with size of square
                curr[i] = min(prev[i-1], prev[i], curr[i-1]) + 1
                if curr[i] > max_square:
                    max_square = curr[i]
        prev = curr
    return max_square if max_square != 0 else max(prev)  # just in case only one row

def main(_):
    while True:
        try:
            n = int(input())
            if n == 0:
                break
            lines = [input() for _ in range(n)]
            print(largest_square(lines))
        except EOFError:
            break

if __name__ == "__main__":
    main(sys.argv)