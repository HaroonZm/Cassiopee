import sys

def find_square(data):
    max_size = 0
    lmap = []
    for row in data:
        temp = []
        for c in row:
            if c == '.':
                temp.append(1)
            else:
                temp.append(0)
        lmap.append(temp)
    prev_row = lmap[0]
    for curr_row in lmap[1:]:
        for x in range(1, len(lmap[0])):
            if curr_row[x] == 1:
                if prev_row[x - 1] != 0 and prev_row[x] != 0 and curr_row[x - 1] != 0:
                    curr_row[x] = min(prev_row[x - 1], min(prev_row[x], curr_row[x - 1])) + 1
                    if curr_row[x] > max_size:
                        max_size = curr_row[x]
        prev_row = curr_row
    return max_size

def find_square2(data):
    max_size = 0
    lmap = []
    for row in data:
        temp = []
        for c in row:
            if c == '.':
                temp.append(1)
            else:
                temp.append(0)
        lmap.append(temp)
    prev_row = lmap[0]
    for curr_row in lmap[1:]:
        for x, t in enumerate(curr_row[1:], start=1):
            if t == 1:
                curr_row[x] = min(prev_row[x - 1], min(prev_row[x], curr_row[x - 1])) + 1
                if curr_row[x] > max_size:
                    max_size = curr_row[x]
        prev_row = curr_row
    return max_size

def main(args):
    while True:
        n = int(input())
        if n == 0:
            break
        data = [input() for _ in range(n)]
        result = find_square2(data)
        print(result)

if __name__ == '__main__':
    main(sys.argv[1:])